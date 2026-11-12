# okapi-python
A client library for accessing OKAPI (https://github.com/50Bytes-dev/okapi), the gateway that holds logins into
personal OK.ru (Odnoklassniki) accounts and works from them through OK's web messenger: login by OK's own QR code,
scanned in the OK app; sending text and photos to people and chats with idempotency by `ref`; editing and deleting
messages; history, read marks, typing; chats, their members, users; and incoming events as signed webhooks. One
gateway serves many accounts; an account is a token, a webhook, a proxy and one OK login. This package follows
okapi's version (0.1.0).

The package is generated from the gateway's OpenAPI schema (`static/api/spec.yml` in okapi; the gateway serves it at
`/api/spec.yml`, with the Swagger UI at `/api/`). The full contract, with every code and when it comes, is
[`API.md`](https://github.com/50Bytes-dev/okapi/blob/main/API.md).

## Clients
Every call but `GET /health` carries `Authorization: Bearer <token>`: the admin token on `/admin/*`, the account's
token everywhere else. `AuthenticatedClient` sends exactly that by default:

```python
import httpx

from okapi_python import AuthenticatedClient, Client

# /admin/*: the admin token (OKAPI_ADMIN_TOKEN)
admin = AuthenticatedClient(base_url="http://localhost:5560", token="<admin token>")

# everything else: the account token from create_account (or rotate_account_token)
account = AuthenticatedClient(
    base_url="http://localhost:5560",
    token="<account token>",
    timeout=httpx.Timeout(30.0),
)

# /health takes no token
public = Client(base_url="http://localhost:5560")
```

A missing or wrong token answers `401 unauthorized`; on an account route it also means the account was deleted. The
clients leave `token` and their headers out of `repr`, and the answers that carry a new account token or webhook
secret (`CreateAccountResponse`, `AccountTokenResponse`, `WebhookSecretResponse`) leave those fields out of theirs,
so a client or an answer in a log or a traceback does not show them.

### Timeouts
httpx's default timeout of 5 s is too short for the account client: the gateway bounds each call to OK at 10 s and
answers `504 timeout` past it. Its own budgets:

| Call | Gateway's budget |
|---|---|
| `send_message` | at most two attempts of 10 s each within 25 s |
| `edit_message`, `delete_messages` | the messages are read first, then changed: two calls to OK of up to 10 s each |
| `list_chats` | reads OK's pages until it has `limit` chats, at most 10 per request, each call up to 10 s; with `type_` or `q` it skips the chats that do not match, so it reads more |
| `get_chat`, `list_members`, `get_history`, `get_message`, `get_user`, `get_users`, `mark_read` | one or two calls to OK of up to 10 s each |
| `connect` | waits up to 10 s for the connection, then answers `connected: false` and goes on connecting; up to 5 s more when OK no longer accepts the login |
| `upload_media` | a `url` is fetched within 10 s; the upload to OK takes up to 120 s |
| `start_qr_login` | waits for ok.ru to give a QR, bounded only by `OKAPI_LOGIN_TIMEOUT` (10 min by default) |

The gateway's HTTP server reads a request within 120 s and writes its answer within 300 s.

A timeout of 30 s covers a send and the calls of one or two OK calls. Give `upload_media`, `start_qr_login` and a
`list_chats` with `type_` or `q` a client of their own with a longer timeout:

```python
slow = AuthenticatedClient(base_url="http://localhost:5560", token="<account token>", timeout=httpx.Timeout(150.0))
```

A client that gives up before the gateway answers knows as little as a `504 timeout`: the call may have taken effect.
For a send, repeat it with the same `ref` (see [Send](#send-a-message)).

## Calls
Every operation is a module under `okapi_python.api.<tag>` with four functions: `sync`, `sync_detailed`, `asyncio`
and `asyncio_detailed`. `sync` returns the parsed body, which for an error is an `ErrorResponse`; `sync_detailed`
returns a `Response` with `status_code` and `parsed`.

| Module | Call |
|---|---|
| `api.health.get_health` | `GET /health` |
| `api.admin.list_accounts` | `GET /admin/accounts` |
| `api.admin.create_account` | `POST /admin/accounts` |
| `api.admin.get_account` | `GET /admin/accounts/{accountId}` |
| `api.admin.update_account` | `PATCH /admin/accounts/{accountId}` |
| `api.admin.delete_account` | `DELETE /admin/accounts/{accountId}` |
| `api.admin.rotate_account_token` | `POST /admin/accounts/{accountId}/token` |
| `api.session.get_session` | `GET /session` |
| `api.session.connect` | `POST /session/connect` |
| `api.session.disconnect` | `POST /session/disconnect` |
| `api.session.logout` | `POST /session/logout` |
| `api.session.resume` | `POST /session/resume` |
| `api.login.get_login` | `GET /session/login` |
| `api.login.cancel_login` | `DELETE /session/login` |
| `api.login.start_qr_login` | `POST /session/login/qr` |
| `api.webhook.get_webhook` | `GET /webhook` |
| `api.webhook.set_webhook` | `PUT /webhook` |
| `api.webhook.delete_webhook` | `DELETE /webhook` |
| `api.webhook.rotate_webhook_secret` | `POST /webhook/secret` |
| `api.media.upload_media` | `POST /media` |
| `api.messages.send_message` | `POST /messages` |
| `api.messages.get_message` | `GET /chats/{chatId}/messages/{messageId}` |
| `api.messages.edit_message` | `PATCH /chats/{chatId}/messages/{messageId}` |
| `api.messages.delete_messages` | `POST /chats/{chatId}/messages/delete` |
| `api.chats.list_chats` | `GET /chats` |
| `api.chats.get_chat` | `GET /chats/{chatId}` |
| `api.chats.list_members` | `GET /chats/{chatId}/members` |
| `api.chats.get_history` | `GET /chats/{chatId}/messages` |
| `api.chats.mark_read` | `POST /chats/{chatId}/read` |
| `api.chats.send_typing` | `POST /chats/{chatId}/typing` |
| `api.users.get_users` | `GET /users` |
| `api.users.get_user` | `GET /users/{userId}` |

Fields the gateway leaves out are `UNSET` (`from okapi_python.types import UNSET`), which is falsy. `chat_id` and
user ids are `int`; a message id is a `str` of digits (OK's ids have 18 digits). A dialog's chat id is positive, a
group chat's negative.

## Errors
Every error is the envelope `{"success": false, "code": "...", "error": "...", ...}`, parsed as `ErrorResponse`.
Branch on `code` (and the HTTP status), never on `error`: it is a fixed English text per case. The details come with
the codes that name them: `upstream_code` (OK's error string, e.g. `chat.denied`), `pause` (`409 paused`) and
`rejected_attachments` (`attachment_rejected`). `retryAfterMs` (`502 upload_failed` while the gateway is busy with
other photos) is not in the schema's `ErrorResponse`: read it as `res.additional_properties.get("retryAfterMs")`.

An envelope parses as `ErrorResponse` on any status of 400 and above, also one the schema does not list for that call.
Another body on an unlisted status is `None` (or `errors.UnexpectedStatus` with `raise_on_unexpected_status=True`);
a body that is not JSON on a listed status (a proxy's page in front of the gateway) raises `json.JSONDecodeError`.

```python
from okapi_python.api.chats import get_chat
from okapi_python.models import ErrorResponse

res = get_chat.sync(-123456789012345, client=account)
if isinstance(res, ErrorResponse):
    if res.code == "not_connected":  # 503: nothing reached OK; repeating cannot double anything
        ...
    elif res.code == "timeout":  # 504: it reached OK and no answer came; its effect is unknown
        ...
    elif res.code == "paused":  # 409: the OK user is paused; acting calls are refused until resume
        print(res.pause.reason, res.pause.upstream_code, res.pause.since)
    else:  # not_logged_in, peer_not_found, write_forbidden, upstream_error, ...
        raise RuntimeError(f"{res.code}: {res.error}")
```

The codes and their statuses are in API.md's [Errors](https://github.com/50Bytes-dev/okapi/blob/main/API.md#errors).

## Create an account

```python
from okapi_python.api.admin import create_account, delete_account
from okapi_python.models import CreateAccountRequest, EventType

created = create_account.sync(
    client=admin,
    body=CreateAccountRequest(
        name="shop-1",
        webhook_url="https://example.com/okapi/events",
        events=[EventType.ALL],
        proxy="socks5://user:password@10.0.0.5:1080",  # optional; "" or absent = direct
    ),
)
# Both are shown only here: store them. A lost token is replaced by rotate_account_token,
# a lost secret by api.webhook.rotate_webhook_secret.
print(created.account.id, created.token, created.webhook_secret)

delete_account.sync(created.account.id, client=admin)
```

## Log in by QR code
OK's own QR login of ok.ru, confirmed in the OK app. There is no phone or password login.

```python
from okapi_python.api.login import get_login, start_qr_login
from okapi_python.api.session import get_session
from okapi_python.models import ErrorResponse, LoginStep

res = start_qr_login.sync(client=slow)  # a running login is cancelled first
if isinstance(res, ErrorResponse):
    # already_logged_in (409): log out first; login_unavailable (503): ok.ru gave no QR, try again later
    raise RuntimeError(res.code)

qr = res.login.qr
show_qr(qr.image)  # your code: a PNG data URL; qr.link opens the login on the phone where the OK app is
tell_owner(qr.code)  # your code: confirm in the app only if it shows this 4-digit code

# Follow LoginUpdated (see Webhooks), or poll every 1-2 s:
login = get_login.sync(client=account).login
if login.step == LoginStep.DONE:  # the session connects; Connected follows
    print("logged in as", login.ok_user.name)
elif login.step == LoginStep.FAILED:
    print("login failed:", login.failure.reason)  # expired, cancelled, unavailable, verification_required, failed

session = get_session.sync(client=account)
print(session.logged_in, session.connected, session.pause)
```

A login not confirmed within `OKAPI_LOGIN_TIMEOUT` (10 min by default, `login.expires_at`) fails `expired`.
`api.login.cancel_login` cancels a running one. The QR, its link and its code are the only login data the gateway
ever shows, and only to the account itself.

`api.session.connect` starts the stored login's session (and keeps it up across restarts), `disconnect` closes it
(the login stays stored), `logout` erases the stored login.

## Send a message

```python
from okapi_python.api.messages import send_message
from okapi_python.models import ErrorResponse, SendMessageRequest

res = send_message.sync(
    client=account,
    body=SendMessageRequest(chat_id=-123456789012345, text="Hello!", ref="order-1042-confirm"),
)
# or to a person: SendMessageRequest(user_id=571234567890, ...); the answer carries the dialog's chat_id

if isinstance(res, ErrorResponse):
    if res.code == "timeout":
        ...  # the message may have gone out: send again with the same ref
    elif res.code == "attachment_rejected":
        ...  # upload the handles at res.rejected_attachments anew
    else:
        ...  # not_connected, invalid_target, peer_not_found, write_forbidden, message_rejected, send_rejected, paused
else:
    print(res.chat_id, res.message_id, res.duplicate)
```

Exactly one of `chat_id` and `user_id`; `text`, `attachments` or both. The gateway does not bound the text length or
the number of photos, and keeps no pace and no lock between sends: the pace is yours.

The `ref` (at most 128 bytes) is your idempotency key. Inside one request the gateway makes at most two attempts with
one OK client id (`cid`), which the `ref` fixes; OK answers a repeated `cid` with the first message:

- a repeat of a ref whose message id is known is answered with `duplicate=True`, without calling OK, even while the
  OK user is paused or the session is down;
- a repeat after `504 timeout` sends again with the same `cid`: OK returns the first message if it went out
  (`duplicate=True`);
- after `503 not_connected` (nothing was written) or a refusal by OK, the ref is free again: the next send with it
  is a new send;
- the same ref with another chat is `400 invalid_input`;
- a ref is remembered for 7 days, and only within the login it was sent under.

Without a ref, a repeat after `timeout` may double the message.

## Photos
A photo is uploaded once with `POST /media` and sent by its handle. The handle is valid in any chat of the same OK
user: upload once, send many times.

```python
from okapi_python.api.media import upload_media
from okapi_python.api.messages import send_message
from okapi_python.models import ErrorResponse, SendMessageRequest, UploadMediaForm, UploadMediaRequest
from okapi_python.types import File

# multipart, the field `file`
with open("photo.jpg", "rb") as f:
    up = upload_media.sync(client=slow, body=UploadMediaForm(file=File(payload=f, file_name="photo.jpg")))

# or JSON with exactly one of url (fetched by the gateway) and data (base64 or a base64 data URL)
up = upload_media.sync(client=slow, body=UploadMediaRequest(url="https://example.com/photo.jpg"))

if isinstance(up, ErrorResponse):
    ...  # invalid_input, invalid_media, body_too_large, fetch_failed, upload_failed, paused, not_connected, timeout
else:
    print(up.attachment, up.width, up.height, up.size)
    send_message.sync(
        client=account,
        body=SendMessageRequest(chat_id=-123456789012345, text="Платье, 1200 ₽", attachments=[up.attachment]),
    )
```

The gateway decodes the photo, applies its EXIF orientation and re-encodes it as a JPEG within OK's limits (1680×1680
px at quality 0.8 by default). A side under 64 px is `invalid_media`. Photos only.

## Messages and chats

```python
from okapi_python.api.chats import get_history, list_chats, list_members, mark_read
from okapi_python.api.messages import delete_messages, edit_message
from okapi_python.models import ChatType, DeleteMessagesRequest, EditMessageRequest, MarkReadRequest
from okapi_python.types import UNSET

# All chats, newest event first; only a missing next_cursor means the end
cursor = UNSET
while True:
    page = list_chats.sync(client=account, cursor=cursor, limit=50)
    for chat in page.chats:
        print(chat.chat_id, chat.type_, chat.title)
    if not page.next_cursor:
        break
    cursor = page.next_cursor

# Group chats whose title matches (a page may hold fewer than limit chats, even none, and still go on)
found = list_chats.sync(client=slow, type_=[ChatType.CHAT], q="Test Group")

members = list_members.sync(-123456789012345, client=account)  # members.members: user_id, name, role
history = get_history.sync(-123456789012345, client=account, limit=50)  # newest first; before=history.next_cursor

edit_message.sync(-123456789012345, "116512345678901234", client=account, body=EditMessageRequest(text="Fixed"))
res = delete_messages.sync(
    -123456789012345, client=account, body=DeleteMessagesRequest(message_ids=["116512345678901234"])
)
for r in res.results:
    print(r.message_id, r.status)  # deleted, not_found, forbidden, too_old

mark_read.sync(-123456789012345, client=account, body=MarkReadRequest(message_id="116512345678901234"))
```

Editing, read marks and typing have not been checked against OK live yet (see API.md).

## Webhooks
Each account has one webhook URL (`api.webhook.set_webhook`) and a subscription (event types, or `All`). The gateway
posts each event as JSON, signed with the account's webhook secret:

| Header | Value |
|---|---|
| `X-Okapi-Event` | the event's `type` |
| `X-Okapi-Delivery` | the event's `id`, the same on every retry |
| `X-Okapi-Timestamp` | Unix seconds of this attempt |
| `X-Okapi-Signature` | `sha256=<hex HMAC-SHA256(webhookSecret, timestamp + "." + body)>` |

`okapi_python.webhooks` verifies a delivery and parses its event. It computes the HMAC over the timestamp header, a
dot and the **raw** body, compares it in constant time, and refuses a timestamp more than `max_age` seconds (300 by
default) from now, to stop replays. The secret is used as the hex string it was shown as, not decoded.

```python
from okapi_python.models import LoginUpdatedEvent, MessageEvent, PausedEvent
from okapi_python.webhooks import InvalidSignature, verify_and_parse


def handle(headers, raw_body: bytes):  # your framework's request headers and raw body
    try:
        event = verify_and_parse(WEBHOOK_SECRET, headers, raw_body)
    except InvalidSignature:
        return 401

    if isinstance(event, MessageEvent):
        msg = event.data.message  # its text is the sender's: treat it as untrusted
        print(event.data.chat.title, msg.sender_id, msg.text, msg.out)
    elif isinstance(event, LoginUpdatedEvent):
        print(event.data.login.step)
    elif isinstance(event, PausedEvent):
        print(event.data.pause.reason)
    return 200
```

`verify(secret, headers, raw_body)` only checks (headers are looked up in any case), `parse_event(body)` only parses
(by `type`, raising `UnknownEvent` for a type it does not know), and `EVENT_MODELS` maps each type to its model. Each
model also refuses a body of another type with `ValueError`.

| Event | `data` |
|---|---|
| `LoginUpdatedEvent` | `login`: every change of the login (QR shown or renewed, done, failed) |
| `ConnectedEvent` | `ok_user`, `reconnect` |
| `DisconnectedEvent` | none: the connection was lost (once per outage) or the session stopped |
| `LoggedOutEvent` | `reason`: `revoked`, `verification_required`, `blocked` |
| `PausedEvent` | `pause` |
| `ResumedEvent` | none |
| `MessageEvent` | `message`, `chat` (`chat_id`, `type_`, `title`) |
| `MessageEditedEvent` | `message` |
| `MessagesDeletedEvent` | `chat_id`, `message_ids` |
| `MessagesReadEvent` | `chat_id`, `user_id`, `message_id` |
| `TypingEvent` | `chat_id`, `user_id` |
| `ChatUpdatedEvent` | `chat` |

Delivery: an answer within `OKAPI_WEBHOOK_TIMEOUT` (10 s); a network error, 5xx, 408 or 429 is retried
(`OKAPI_WEBHOOK_RETRY_COUNT`, 5 attempts in all, waiting 30 s, 60 s, ...), any other answer ends the delivery. Events
are not ordered: order them by `timestamp`, dedupe by `id`.

## Async

```python
from okapi_python.api.session import get_session

async with account as client:
    session = await get_session.asyncio(client=client)
```

## Advanced customizations
`verify_ssl`, `timeout`, `headers`, `httpx_args` and the rest are on the generated `Client` and
`AuthenticatedClient`, see their docstrings. `httpx_args` goes to the underlying `httpx.Client` or
`httpx.AsyncClient`:

```python
from okapi_python import AuthenticatedClient


def log_response(response):
    request = response.request
    print(f"{request.method} {request.url} - Status {response.status_code}")


account = AuthenticatedClient(
    base_url="http://localhost:5560",
    token="<account token>",
    httpx_args={"event_hooks": {"response": [log_response]}},
)
```

## Regenerate client
After a change of `../okapi/static/api/spec.yml`:

```shell
uv sync
./generate.sh
uv run pytest
uv run ruff check . && uv run ruff format --check .
```

`generate.sh` runs `openapi-python-client` from the dev group and moves the generated `okapi_client` package to
`okapi_python`. `okapi_python/webhooks.py` is hand-written and kept across a regeneration. The generator is pinned
below 0.29: 0.29 writes code that needs Python 3.11 (`typing.Self`), and the package supports 3.10.

Before generating, `generate.sh` drops the `type` keyword of `EventEnvelope`'s `type` and `data` in a copy of the
schema. Each event is `allOf` the envelope and its own `type` (a const) and `data`; the generator cannot merge a
string with a const (it drops the event) and of two `data` objects keeps the envelope's empty one. Each event narrows
both fields, so the copy accepts the same bodies.

The templates override three of the generator's:

- `templates/client.py.jinja`: `token` and the headers (which carry the token once a request is made) are left out
  of the clients' `repr`.
- `templates/model.py.jinja`: the fields that carry a secret (`token`, `webhook_secret`) are left out of the model's
  `repr`.
- `templates/endpoint_module.py.jinja`: a call that answers `ErrorResponse` parses the envelope on any status of 400
  and above; and for `POST /media`, which takes multipart or JSON, httpx sets the multipart `Content-Type` with its
  boundary, and `Unset`, which the generator's macros use for such a body, is imported.

When the generator is upgraded, copy its new templates and redo these changes.

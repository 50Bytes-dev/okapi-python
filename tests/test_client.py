import json

import httpx
import pytest

from okapi_python import AuthenticatedClient, Client
from okapi_python.api.admin import create_account
from okapi_python.api.albums import list_group_albums, update_group_album, upload_group_album_photo
from okapi_python.api.chats import list_chats
from okapi_python.api.health import get_health
from okapi_python.api.login import start_qr_login
from okapi_python.api.media import upload_media
from okapi_python.api.messages import send_message
from okapi_python.api.session import connect
from okapi_python.models import (
    Album,
    AlbumListResponse,
    AlbumResponse,
    ChatType,
    CreateAccountRequest,
    CreateAccountResponse,
    ErrorResponse,
    EventType,
    HealthResponse,
    LoginResponse,
    LoginStep,
    PauseReason,
    PhotoResponse,
    SendMessageRequest,
    SendMessageResponse,
    UpdateGroupAlbumRequest,
    UploadAlbumPhotoForm,
    UploadMediaForm,
    UploadMediaRequest,
    UploadMediaResponse,
)
from okapi_python.types import UNSET, File

BASE_URL = "http://okapi.test"


class Recorder:
    """A MockTransport handler that answers one status and body and keeps the requests it got."""

    def __init__(self, status: int, body: dict):
        self.status = status
        self.body = body
        self.requests: list[httpx.Request] = []

    def __call__(self, request: httpx.Request) -> httpx.Response:
        request.read()
        self.requests.append(request)
        return httpx.Response(self.status, json=self.body)


def account_client(recorder: Recorder, token: str = "account-token") -> AuthenticatedClient:
    return AuthenticatedClient(base_url=BASE_URL, token=token, httpx_args={"transport": httpx.MockTransport(recorder)})


def test_a_send_parses_its_answer_with_the_message_id_as_a_string():
    rec = Recorder(
        200,
        {"success": True, "chatId": -123456789012345, "messageId": "116512345678901234", "duplicate": False},
    )
    res = send_message.sync(
        client=account_client(rec),
        body=SendMessageRequest(chat_id=-123456789012345, text="Hello!", ref="order-1042-confirm"),
    )

    assert isinstance(res, SendMessageResponse)
    assert res.message_id == "116512345678901234"
    assert res.chat_id == -123456789012345
    assert res.duplicate is False
    sent = json.loads(rec.requests[0].content)
    assert sent == {"chatId": -123456789012345, "text": "Hello!", "silent": False, "ref": "order-1042-confirm"}
    assert rec.requests[0].url.path == "/messages"


def test_an_error_envelope_parses_with_its_code_and_details():
    rec = Recorder(
        409,
        {
            "success": False,
            "code": "paused",
            "error": "The OK user is paused",
            "pause": {"reason": "spam", "upstreamCode": "error.flood", "since": 1794500000},
        },
    )
    res = send_message.sync_detailed(
        client=account_client(rec), body=SendMessageRequest(user_id=571234567890, text="Hi")
    )

    assert res.status_code == 409
    assert isinstance(res.parsed, ErrorResponse)
    assert res.parsed.code == "paused"
    assert res.parsed.pause.reason == PauseReason.SPAM
    assert res.parsed.upstream_code is UNSET


def test_rejected_attachments_come_with_their_indexes():
    rec = Recorder(
        422,
        {
            "success": False,
            "code": "attachment_rejected",
            "error": "An attachment handle is unusable",
            "rejectedAttachments": [0, 2],
        },
    )
    res = send_message.sync(
        client=account_client(rec), body=SendMessageRequest(chat_id=1, attachments=["okph1.a", "okph1.b", "okph1.c"])
    )

    assert isinstance(res, ErrorResponse)
    assert res.rejected_attachments == [0, 2]


def test_an_error_envelope_on_a_status_the_schema_does_not_list_still_parses():
    # POST /session/connect lists 200, 401, 409 and 500; the gateway may also answer 503 not_connected.
    rec = Recorder(503, {"success": False, "code": "not_connected", "error": "the session did not start"})
    res = connect.sync(client=account_client(rec))

    assert isinstance(res, ErrorResponse)
    assert res.code == "not_connected"


def test_a_body_that_is_not_an_envelope_on_an_unlisted_status_is_none():
    rec = Recorder(418, {"teapot": True})
    assert connect.sync(client=account_client(rec)) is None


def test_the_account_token_goes_as_a_bearer_token():
    rec = Recorder(200, {"success": True, "chats": []})
    page = list_chats.sync(client=account_client(rec, token="0123abcd"), type_=[ChatType.USER, ChatType.CHAT])

    assert page.chats == []
    assert page.next_cursor is UNSET
    request = rec.requests[0]
    assert request.headers["Authorization"] == "Bearer 0123abcd"
    assert request.url.params.get_list("type") == ["user", "chat"]
    assert request.url.params["limit"] == "50"


def test_the_admin_token_goes_as_a_bearer_token_and_the_new_secrets_stay_out_of_repr():
    rec = Recorder(
        200,
        {
            "success": True,
            "account": {
                "id": "6f1c2d4e-8a7b-4c3d-9e2f-1a2b3c4d5e6f",
                "name": "shop-1",
                "webhookUrl": "",
                "events": ["All"],
                "proxy": "",
                "loggedIn": False,
                "connected": False,
                "createdAt": 1794500000,
            },
            "token": "a" * 64,
            "webhookSecret": "b" * 64,
        },
    )
    admin = AuthenticatedClient(
        base_url=BASE_URL, token="admin-token", httpx_args={"transport": httpx.MockTransport(rec)}
    )
    res = create_account.sync(client=admin, body=CreateAccountRequest(name="shop-1", events=[EventType.ALL]))

    assert rec.requests[0].headers["Authorization"] == "Bearer admin-token"
    assert isinstance(res, CreateAccountResponse)
    assert res.token == "a" * 64
    assert res.webhook_secret == "b" * 64
    assert res.account.events == [EventType.ALL]
    assert "a" * 64 not in repr(res)
    assert "b" * 64 not in repr(res)


def test_a_client_leaves_its_token_out_of_repr_also_after_a_request():
    rec = Recorder(200, {"success": True, "chats": []})
    client = account_client(rec, token="secret-account-token")
    list_chats.sync(client=client)

    assert "secret-account-token" not in repr(client)


def test_health_takes_no_token_and_parses_the_degraded_answer():
    rec = Recorder(
        503,
        {
            "success": False,
            "status": "degraded",
            "version": "0.1.1",
            "uptimeSeconds": 12,
            "db": False,
            "accounts": 0,
            "connected": 0,
        },
    )
    public = Client(base_url=BASE_URL, httpx_args={"transport": httpx.MockTransport(rec)})
    res = get_health.sync(client=public)

    assert "Authorization" not in rec.requests[0].headers
    assert isinstance(res, HealthResponse)
    assert res.status.value == "degraded"
    assert res.db is False


def test_a_multipart_upload_lets_httpx_set_its_boundary():
    rec = Recorder(200, {"success": True, "attachment": "okph1.eyJwIjoi", "width": 1280, "height": 960, "size": 183402})
    res = upload_media.sync(
        client=account_client(rec),
        body=UploadMediaForm(file=File(payload=b"\xff\xd8\xff", file_name="photo.jpg", mime_type="image/jpeg")),
    )

    assert isinstance(res, UploadMediaResponse)
    assert res.attachment == "okph1.eyJwIjoi"
    content_type = rec.requests[0].headers["Content-Type"]
    assert content_type.startswith("multipart/form-data; boundary=")
    assert b'name="file"; filename="photo.jpg"' in rec.requests[0].content


def test_a_json_upload_is_sent_as_json():
    rec = Recorder(
        422, {"success": False, "code": "fetch_failed", "error": "the url could not be fetched: internal address"}
    )
    res = upload_media.sync(client=account_client(rec), body=UploadMediaRequest(url="https://example.com/photo.jpg"))

    assert isinstance(res, ErrorResponse)
    assert res.code == "fetch_failed"
    assert rec.requests[0].headers["Content-Type"] == "application/json"
    assert json.loads(rec.requests[0].content) == {"url": "https://example.com/photo.jpg"}


def test_a_busy_gateway_tells_when_to_upload_again():
    rec = Recorder(
        502,
        {
            "success": False,
            "code": "upload_failed",
            "error": "the gateway is busy with other photos; try again",
            "retryAfterMs": 1000,
        },
    )
    res = upload_media.sync(client=account_client(rec), body=UploadMediaRequest(url="https://example.com/photo.jpg"))

    assert isinstance(res, ErrorResponse)
    assert res.code == "upload_failed"
    assert res.retry_after_ms == 1000
    assert "retryAfterMs" not in res.additional_properties


def test_an_album_photo_goes_with_its_description_in_one_form():
    rec = Recorder(
        200,
        {
            "success": True,
            "photo": {
                "photoId": "1011463854865",
                "albumId": "1011463757073",
                "groupId": 70000060985873,
                "description": "Куртка, 46",
                "width": 1200,
                "height": 900,
            },
        },
    )
    res = upload_group_album_photo.sync(
        70000060985873,
        "1011463757073",
        client=account_client(rec),
        body=UploadAlbumPhotoForm(
            file=File(payload=b"\xff\xd8\xff", file_name="photo.jpg", mime_type="image/jpeg"), description="Куртка, 46"
        ),
    )

    assert isinstance(res, PhotoResponse)
    assert res.photo.photo_id == "1011463854865"
    assert res.photo.description == "Куртка, 46"
    req = rec.requests[0]
    assert req.url.path == "/groups/70000060985873/albums/1011463757073/photos"
    assert req.headers["Content-Type"].startswith("multipart/form-data; boundary=")
    assert b'name="file"; filename="photo.jpg"' in req.content
    assert b'name="description"' in req.content and "Куртка, 46".encode() in req.content


def test_a_photo_whose_description_failed_is_named_in_the_error():
    rec = Recorder(
        502,
        {
            "success": False,
            "code": "description_failed",
            "error": "the photo is uploaded, its description is not; set it with PATCH",
            "photoId": "1011463854865",
        },
    )
    res = upload_group_album_photo.sync(
        70000060985873,
        "1011463757073",
        client=account_client(rec),
        body=UploadAlbumPhotoForm(file=File(payload=b"\xff\xd8\xff", file_name="photo.jpg"), description="x"),
    )

    assert isinstance(res, ErrorResponse)
    assert res.code == "description_failed"
    assert res.photo_id == "1011463854865"


def test_an_album_list_leaves_the_settings_it_did_not_read_unset():
    rec = Recorder(
        200,
        {
            "success": True,
            "albums": [{"albumId": "1011463757073", "groupId": 70000060985873, "title": "Товары", "photosCount": 2}],
        },
    )
    res = list_group_albums.sync(70000060985873, client=account_client(rec))

    assert isinstance(res, AlbumListResponse)
    album = res.albums[0]
    assert isinstance(album, Album)
    assert (album.album_id, album.group_id, album.photos_count) == ("1011463757073", 70000060985873, 2)
    assert album.pinned is UNSET and album.admins_only is UNSET and album.visibility is UNSET


def test_an_album_change_sends_only_the_fields_it_names():
    rec = Recorder(
        200,
        {
            "success": True,
            "album": {
                "albumId": "1011463757073",
                "groupId": 70000060985873,
                "title": "Товары",
                "pinned": True,
                "adminsOnly": False,
            },
        },
    )
    res = update_group_album.sync(
        70000060985873, "1011463757073", client=account_client(rec), body=UpdateGroupAlbumRequest(pinned=True)
    )

    assert isinstance(res, AlbumResponse)
    assert res.album.pinned is True and res.album.admins_only is False
    assert rec.requests[0].method == "PATCH"
    assert json.loads(rec.requests[0].content) == {"pinned": True}


def test_a_qr_login_answers_the_qr_and_its_code():
    rec = Recorder(
        200,
        {
            "success": True,
            "login": {
                "step": "qr",
                "startedAt": 1794500000,
                "expiresAt": 1794500600,
                "qr": {"image": "data:image/png;base64,iVBORw0KGgo", "link": "https://ok.ru/qrCode/x", "code": "1345"},
            },
        },
    )
    res = start_qr_login.sync(client=account_client(rec))

    assert isinstance(res, LoginResponse)
    assert res.login.step == LoginStep.QR
    assert res.login.qr.code == "1345"
    assert res.login.failure is UNSET


@pytest.mark.parametrize("status", [400, 401, 403, 404, 409, 413, 422, 500, 503, 504])
def test_every_documented_error_status_of_a_send_is_an_error_response(status):
    rec = Recorder(status, {"success": False, "code": "some_code", "error": "text"})
    res = send_message.sync(client=account_client(rec), body=SendMessageRequest(chat_id=1, text="x"))

    assert isinstance(res, ErrorResponse)
    assert res.code == "some_code"

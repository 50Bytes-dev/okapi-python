import hashlib
import hmac
import json

import pytest

from okapi_python.models import (
    ChatType,
    ConnectedEvent,
    DisconnectedEvent,
    EventType,
    LoggedOutEvent,
    LoggedOutEventDataReason,
    LoginStep,
    LoginUpdatedEvent,
    MessageEvent,
    MessagesDeletedEvent,
)
from okapi_python.webhooks import (
    EVENT_MODELS,
    InvalidSignature,
    UnknownEvent,
    parse_event,
    sign,
    verify,
    verify_and_parse,
    verify_signature,
)

SECRET = "5f" * 32  # used as the hex string, not decoded
NOW = 1794500000.0


def envelope(event_type: str, data: dict) -> dict:
    return {
        "id": "0b8e9c1e-3f4a-4c6b-9a57-2f1d8e7c6b5a",
        "type": event_type,
        "accountId": "6f1c2d4e-8a7b-4c3d-9e2f-1a2b3c4d5e6f",
        "accountName": "shop-1",
        "timestamp": 1794500000,
        "data": data,
    }


MESSAGE = envelope(
    "Message",
    {
        "message": {
            "messageId": "116512345678901234",
            "chatId": -123456789012345,
            "senderId": 571234567890,
            "out": False,
            "date": 1794500000000,
            "text": "Hello!",
            "attachments": [{"type": "photo", "photoId": 1234567890, "url": "https://x", "width": 1280, "height": 960}],
            "cid": 1794499999123,
        },
        "chat": {"chatId": -123456789012345, "type": "chat", "title": "Test Group chat"},
    },
)


def delivery(body: dict, timestamp: str = "1794500000", secret: str = SECRET) -> tuple[dict[str, str], bytes]:
    raw = json.dumps(body).encode()
    headers = {
        "X-Okapi-Event": body["type"],
        "X-Okapi-Delivery": body["id"],
        "X-Okapi-Timestamp": timestamp,
        "X-Okapi-Signature": sign(secret, timestamp, raw),
    }
    return headers, raw


def test_the_signature_is_the_hmac_of_the_timestamp_a_dot_and_the_body_under_the_hex_secret():
    raw = b'{"type":"Resumed"}'
    want = "sha256=" + hmac.new(SECRET.encode(), b"1794500000." + raw, hashlib.sha256).hexdigest()

    assert sign(SECRET, "1794500000", raw) == want


def test_a_signed_delivery_verifies():
    headers, raw = delivery(MESSAGE)

    assert verify(SECRET, headers, raw, now=NOW)


def test_headers_are_found_in_any_case():
    headers, raw = delivery(MESSAGE)
    lowered = {k.lower(): v for k, v in headers.items()}

    assert verify(SECRET, lowered, raw, now=NOW)


def test_another_secret_a_changed_body_or_a_changed_timestamp_fail():
    headers, raw = delivery(MESSAGE)

    assert not verify("6a" * 32, headers, raw, now=NOW)
    assert not verify(SECRET, headers, raw.replace(b"Hello!", b"Hallo!"), now=NOW)
    moved = dict(headers, **{"X-Okapi-Timestamp": "1794500001"})
    assert not verify(SECRET, moved, raw, now=NOW)


def test_a_timestamp_older_or_newer_than_the_max_age_fails():
    headers, raw = delivery(MESSAGE)

    assert verify(SECRET, headers, raw, now=NOW + 300)
    assert not verify(SECRET, headers, raw, now=NOW + 301)
    assert not verify(SECRET, headers, raw, now=NOW - 301)
    assert verify(SECRET, headers, raw, now=NOW + 3600, max_age=3600)


def test_missing_headers_or_a_timestamp_that_is_no_number_fail():
    headers, raw = delivery(MESSAGE)

    assert not verify(SECRET, {"X-Okapi-Timestamp": headers["X-Okapi-Timestamp"]}, raw, now=NOW)
    assert not verify_signature(SECRET, "soon", headers["X-Okapi-Signature"], raw, now=NOW)


def test_verify_and_parse_refuses_a_bad_signature():
    headers, raw = delivery(MESSAGE, secret="00" * 32)

    with pytest.raises(InvalidSignature):
        verify_and_parse(SECRET, headers, raw, now=NOW)


def test_a_message_event_parses_with_its_chat():
    headers, raw = delivery(MESSAGE)
    event = verify_and_parse(SECRET, headers, raw, now=NOW)

    assert isinstance(event, MessageEvent)
    assert event.data.message.message_id == "116512345678901234"
    assert event.data.message.attachments[0].photo_id == 1234567890
    assert event.data.chat.type_ == ChatType.CHAT
    assert str(event.account_id) == "6f1c2d4e-8a7b-4c3d-9e2f-1a2b3c4d5e6f"


@pytest.mark.parametrize(
    ("body", "model"),
    [
        (
            envelope(
                "LoginUpdated",
                {"login": {"step": "failed", "startedAt": 1, "expiresAt": 2, "failure": {"reason": "expired"}}},
            ),
            LoginUpdatedEvent,
        ),
        (
            envelope(
                "Connected",
                {
                    "okUser": {
                        "id": 571234567890,
                        "name": "Anna Petrova",
                        "firstName": "Anna",
                        "lastName": "Petrova",
                        "profileUrl": "https://ok.ru/profile/571234567890",
                    },
                    "reconnect": True,
                },
            ),
            ConnectedEvent,
        ),
        (envelope("Disconnected", {}), DisconnectedEvent),
        (envelope("LoggedOut", {"reason": "revoked"}), LoggedOutEvent),
        (envelope("MessagesDeleted", {"chatId": 1, "messageIds": ["116512345678901234"]}), MessagesDeletedEvent),
    ],
)
def test_each_event_parses_into_its_model(body, model):
    event = parse_event(json.dumps(body))

    assert isinstance(event, model)


def test_event_data_fields_are_typed():
    login = parse_event(
        envelope("LoginUpdated", {"login": {"step": "qr", "qr": {"image": "data:,", "link": "l", "code": "1345"}}})
    )
    logged_out = parse_event(envelope("LoggedOut", {"reason": "blocked"}))

    assert login.data.login.step == LoginStep.QR
    assert logged_out.data.reason == LoggedOutEventDataReason.BLOCKED


def test_every_event_type_but_all_has_a_model():
    assert set(EVENT_MODELS) == {t.value for t in EventType if t != EventType.ALL}


def test_an_unknown_event_type_is_refused():
    with pytest.raises(UnknownEvent):
        parse_event(envelope("Unknown", {}))


def test_a_model_refuses_a_body_of_another_type():
    with pytest.raises(ValueError):
        MessageEvent.from_dict(envelope("Typing", {"chatId": 1, "userId": 2}))

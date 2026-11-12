from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SendMessageRequest")


@_attrs_define
class SendMessageRequest:
    """Exactly one of `chatId` and `userId`; `text`, `attachments` or both.

    Attributes:
        chat_id (int | Unset):  Example: -123456789012345.
        user_id (int | Unset): Sends to the dialog with this OK user
        text (str | Unset):  Example: Hello!.
        attachments (list[str] | Unset): Handles from `POST /media` Example: ['okph1.eyJwIjoi…'].
        reply_to (str | Unset): The message id this one answers
        silent (bool | Unset): Send without a notification Default: False.
        ref (str | Unset): The idempotency key (at most 128 bytes); see "Sends" above Example: order-1042-confirm.
    """

    chat_id: int | Unset = UNSET
    user_id: int | Unset = UNSET
    text: str | Unset = UNSET
    attachments: list[str] | Unset = UNSET
    reply_to: str | Unset = UNSET
    silent: bool | Unset = False
    ref: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        chat_id = self.chat_id

        user_id = self.user_id

        text = self.text

        attachments: list[str] | Unset = UNSET
        if not isinstance(self.attachments, Unset):
            attachments = self.attachments

        reply_to = self.reply_to

        silent = self.silent

        ref = self.ref

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if chat_id is not UNSET:
            field_dict["chatId"] = chat_id
        if user_id is not UNSET:
            field_dict["userId"] = user_id
        if text is not UNSET:
            field_dict["text"] = text
        if attachments is not UNSET:
            field_dict["attachments"] = attachments
        if reply_to is not UNSET:
            field_dict["replyTo"] = reply_to
        if silent is not UNSET:
            field_dict["silent"] = silent
        if ref is not UNSET:
            field_dict["ref"] = ref

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        chat_id = d.pop("chatId", UNSET)

        user_id = d.pop("userId", UNSET)

        text = d.pop("text", UNSET)

        attachments = cast(list[str], d.pop("attachments", UNSET))

        reply_to = d.pop("replyTo", UNSET)

        silent = d.pop("silent", UNSET)

        ref = d.pop("ref", UNSET)

        send_message_request = cls(
            chat_id=chat_id,
            user_id=user_id,
            text=text,
            attachments=attachments,
            reply_to=reply_to,
            silent=silent,
            ref=ref,
        )

        send_message_request.additional_properties = d
        return send_message_request

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties

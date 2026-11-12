from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.message_status import MessageStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.message_attachment import MessageAttachment


T = TypeVar("T", bound="Message")


@_attrs_define
class Message:
    """A message. Its text is the sender's: treat it as untrusted.
    `status` is `edited` or `removed` when OK marks it so.

        Attributes:
            message_id (str):  Example: 116512345678901234.
            chat_id (int):  Example: -123456789012345.
            sender_id (int):  Example: 571234567890.
            out (bool): Sent by the account's OK user (from this gateway or another device)
            date (int): Unix time in milliseconds Example: 1794500000000.
            text (str):  Example: Hello!.
            attachments (list[MessageAttachment]):
            cid (int): The client id the sender gave the message; a send with `ref` fixes it
            status (MessageStatus | Unset):
            reply_to (str | Unset): The message this one answers
    """

    message_id: str
    chat_id: int
    sender_id: int
    out: bool
    date: int
    text: str
    attachments: list[MessageAttachment]
    cid: int
    status: MessageStatus | Unset = UNSET
    reply_to: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        message_id = self.message_id

        chat_id = self.chat_id

        sender_id = self.sender_id

        out = self.out

        date = self.date

        text = self.text

        attachments = []
        for attachments_item_data in self.attachments:
            attachments_item = attachments_item_data.to_dict()
            attachments.append(attachments_item)

        cid = self.cid

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        reply_to = self.reply_to

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "messageId": message_id,
                "chatId": chat_id,
                "senderId": sender_id,
                "out": out,
                "date": date,
                "text": text,
                "attachments": attachments,
                "cid": cid,
            }
        )
        if status is not UNSET:
            field_dict["status"] = status
        if reply_to is not UNSET:
            field_dict["replyTo"] = reply_to

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.message_attachment import MessageAttachment

        d = dict(src_dict)
        message_id = d.pop("messageId")

        chat_id = d.pop("chatId")

        sender_id = d.pop("senderId")

        out = d.pop("out")

        date = d.pop("date")

        text = d.pop("text")

        attachments = []
        _attachments = d.pop("attachments")
        for attachments_item_data in _attachments:
            attachments_item = MessageAttachment.from_dict(attachments_item_data)

            attachments.append(attachments_item)

        cid = d.pop("cid")

        _status = d.pop("status", UNSET)
        status: MessageStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = MessageStatus(_status)

        reply_to = d.pop("replyTo", UNSET)

        message = cls(
            message_id=message_id,
            chat_id=chat_id,
            sender_id=sender_id,
            out=out,
            date=date,
            text=text,
            attachments=attachments,
            cid=cid,
            status=status,
            reply_to=reply_to,
        )

        message.additional_properties = d
        return message

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

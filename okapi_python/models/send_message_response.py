from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="SendMessageResponse")


@_attrs_define
class SendMessageResponse:
    """
    Attributes:
        success (bool):
        chat_id (int): The chat the message is in (the dialog's id for a `userId` send)
        message_id (str):  Example: 116512345678901234.
        duplicate (bool): The `ref` was sent before; this is the first message
    """

    success: bool
    chat_id: int
    message_id: str
    duplicate: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        chat_id = self.chat_id

        message_id = self.message_id

        duplicate = self.duplicate

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "success": success,
                "chatId": chat_id,
                "messageId": message_id,
                "duplicate": duplicate,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        success = d.pop("success")

        chat_id = d.pop("chatId")

        message_id = d.pop("messageId")

        duplicate = d.pop("duplicate")

        send_message_response = cls(
            success=success,
            chat_id=chat_id,
            message_id=message_id,
            duplicate=duplicate,
        )

        send_message_response.additional_properties = d
        return send_message_response

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

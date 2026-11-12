from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.event_chat import EventChat
    from ..models.message import Message


T = TypeVar("T", bound="MessageEventData")


@_attrs_define
class MessageEventData:
    """
    Attributes:
        message (Message): A message. Its text is the sender's: treat it as untrusted.
            `status` is `edited` or `removed` when OK marks it so.
        chat (EventChat): The chat of a message event. When OK does not tell the chat in time
            (2 s), `title` is empty and `type` is what the id suggests:
            positive `user`, negative `chat`, the account's own id `self`.
    """

    message: Message
    chat: EventChat
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        message = self.message.to_dict()

        chat = self.chat.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "message": message,
                "chat": chat,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.event_chat import EventChat
        from ..models.message import Message

        d = dict(src_dict)
        message = Message.from_dict(d.pop("message"))

        chat = EventChat.from_dict(d.pop("chat"))

        message_event_data = cls(
            message=message,
            chat=chat,
        )

        message_event_data.additional_properties = d
        return message_event_data

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

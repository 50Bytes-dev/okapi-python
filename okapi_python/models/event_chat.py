from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.chat_type import ChatType

T = TypeVar("T", bound="EventChat")


@_attrs_define
class EventChat:
    """The chat of a message event. When OK does not tell the chat in time
    (2 s), `title` is empty and `type` is what the id suggests:
    positive `user`, negative `chat`, the account's own id `self`.

        Attributes:
            chat_id (int):
            type_ (ChatType): `user` (dialog with a person), `self` (dialog with oneself), `chat` (group chat), `group`
                (chat with an OK group), `channel`
            title (str):
    """

    chat_id: int
    type_: ChatType
    title: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        chat_id = self.chat_id

        type_ = self.type_.value

        title = self.title

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "chatId": chat_id,
                "type": type_,
                "title": title,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        chat_id = d.pop("chatId")

        type_ = ChatType(d.pop("type"))

        title = d.pop("title")

        event_chat = cls(
            chat_id=chat_id,
            type_=type_,
            title=title,
        )

        event_chat.additional_properties = d
        return event_chat

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

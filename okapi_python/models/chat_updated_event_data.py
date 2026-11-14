from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.chat import Chat


T = TypeVar("T", bound="ChatUpdatedEventData")


@_attrs_define
class ChatUpdatedEventData:
    """
    Attributes:
        chat (Chat): A chat of the account. `canWrite` is read from the chat as OK lists
            it, by the rules of OK's web client: a chat that is not a dialog and
            is not active, restrictions on input, a group chat whose members OK
            listed in full without the account, a channel the account is neither
            the owner nor a posting admin of. The other side of a dialog may
            still refuse a send (`write_forbidden`).
    """

    chat: Chat
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        chat = self.chat.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "chat": chat,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.chat import Chat

        d = dict(src_dict)
        chat = Chat.from_dict(d.pop("chat"))

        chat_updated_event_data = cls(
            chat=chat,
        )

        chat_updated_event_data.additional_properties = d
        return chat_updated_event_data

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

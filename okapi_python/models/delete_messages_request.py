from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DeleteMessagesRequest")


@_attrs_define
class DeleteMessagesRequest:
    """
    Attributes:
        message_ids (list[str]):
        for_all (bool | Unset): Delete for everyone; false = only for this account Default: True.
    """

    message_ids: list[str]
    for_all: bool | Unset = True
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        message_ids = self.message_ids

        for_all = self.for_all

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "messageIds": message_ids,
            }
        )
        if for_all is not UNSET:
            field_dict["forAll"] = for_all

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        message_ids = cast(list[str], d.pop("messageIds"))

        for_all = d.pop("forAll", UNSET)

        delete_messages_request = cls(
            message_ids=message_ids,
            for_all=for_all,
        )

        delete_messages_request.additional_properties = d
        return delete_messages_request

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

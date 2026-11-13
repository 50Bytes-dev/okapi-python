from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateGroupAlbumRequest")


@_attrs_define
class CreateGroupAlbumRequest:
    """
    Attributes:
        title (str): At most 256 UTF-16 units, not blank Example: Goods.
        pinned (bool | Unset): Show the album first in the group Default: False.
        admins_only (bool | Unset): Only the group's administration adds photos Default: True.
    """

    title: str
    pinned: bool | Unset = False
    admins_only: bool | Unset = True
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        title = self.title

        pinned = self.pinned

        admins_only = self.admins_only

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "title": title,
            }
        )
        if pinned is not UNSET:
            field_dict["pinned"] = pinned
        if admins_only is not UNSET:
            field_dict["adminsOnly"] = admins_only

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        title = d.pop("title")

        pinned = d.pop("pinned", UNSET)

        admins_only = d.pop("adminsOnly", UNSET)

        create_group_album_request = cls(
            title=title,
            pinned=pinned,
            admins_only=admins_only,
        )

        create_group_album_request.additional_properties = d
        return create_group_album_request

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

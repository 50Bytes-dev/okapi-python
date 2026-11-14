from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.group_role import GroupRole
from ..types import UNSET, Unset

T = TypeVar("T", bound="Group")


@_attrs_define
class Group:
    """An OK group of the account's OK user

    Attributes:
        group_id (int):  Example: 70000060985873.
        name (str):  Example: Interest group.
        role (GroupRole): The OK user's role in the group: `moderator` (it owns, administers
            or moderates it, "Модерирую" on OK: it may create, edit and delete
            the group's albums and upload into any), `member` (it uploads where an
            album's `canUpload` says so). OK does not tell an owner from an admin
            or a moderator here.
        photo_url (str | Unset): The group's picture, when its card shows one
    """

    group_id: int
    name: str
    role: GroupRole
    photo_url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        group_id = self.group_id

        name = self.name

        role = self.role.value

        photo_url = self.photo_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "groupId": group_id,
                "name": name,
                "role": role,
            }
        )
        if photo_url is not UNSET:
            field_dict["photoUrl"] = photo_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        group_id = d.pop("groupId")

        name = d.pop("name")

        role = GroupRole(d.pop("role"))

        photo_url = d.pop("photoUrl", UNSET)

        group = cls(
            group_id=group_id,
            name=name,
            role=role,
            photo_url=photo_url,
        )

        group.additional_properties = d
        return group

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

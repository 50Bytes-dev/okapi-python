from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.group_info_status import GroupInfoStatus
from ..models.group_role import GroupRole
from ..types import UNSET, Unset

T = TypeVar("T", bound="GroupInfo")


@_attrs_define
class GroupInfo:
    """A group as its own page shows it: any group the account may see.
    `role` is there when the group is the user's.

        Attributes:
            group_id (int):  Example: 70000060985873.
            name (str): Empty for a deleted group Example: Interest group.
            status (GroupInfoStatus): `active`; `blocked` (OK shows the stub of a blocked group);
                `deleted` (OK has no page of it, as of an id that never was).
                Not checked live: the stubs are matched by OK's wording.
            photo_url (str | Unset):
            role (GroupRole | Unset): The OK user's role in the group: `moderator` (it owns, administers
                or moderates it, "Модерирую" on OK: it may create, edit and delete
                the group's albums and upload into any), `member` (it uploads where an
                album's `canUpload` says so). OK does not tell an owner from an admin
                or a moderator here.
    """

    group_id: int
    name: str
    status: GroupInfoStatus
    photo_url: str | Unset = UNSET
    role: GroupRole | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        group_id = self.group_id

        name = self.name

        status = self.status.value

        photo_url = self.photo_url

        role: str | Unset = UNSET
        if not isinstance(self.role, Unset):
            role = self.role.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "groupId": group_id,
                "name": name,
                "status": status,
            }
        )
        if photo_url is not UNSET:
            field_dict["photoUrl"] = photo_url
        if role is not UNSET:
            field_dict["role"] = role

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        group_id = d.pop("groupId")

        name = d.pop("name")

        status = GroupInfoStatus(d.pop("status"))

        photo_url = d.pop("photoUrl", UNSET)

        _role = d.pop("role", UNSET)
        role: GroupRole | Unset
        if isinstance(_role, Unset):
            role = UNSET
        else:
            role = GroupRole(_role)

        group_info = cls(
            group_id=group_id,
            name=name,
            status=status,
            photo_url=photo_url,
            role=role,
        )

        group_info.additional_properties = d
        return group_info

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

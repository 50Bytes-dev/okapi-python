from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.member import Member


T = TypeVar("T", bound="MemberListResponse")


@_attrs_define
class MemberListResponse:
    """
    Attributes:
        success (bool):
        members (list[Member]):
        next_cursor (str | Unset): The next page; absent on the last
    """

    success: bool
    members: list[Member]
    next_cursor: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        members = []
        for members_item_data in self.members:
            members_item = members_item_data.to_dict()
            members.append(members_item)

        next_cursor = self.next_cursor

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "success": success,
                "members": members,
            }
        )
        if next_cursor is not UNSET:
            field_dict["nextCursor"] = next_cursor

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.member import Member

        d = dict(src_dict)
        success = d.pop("success")

        members = []
        _members = d.pop("members")
        for members_item_data in _members:
            members_item = Member.from_dict(members_item_data)

            members.append(members_item)

        next_cursor = d.pop("nextCursor", UNSET)

        member_list_response = cls(
            success=success,
            members=members,
            next_cursor=next_cursor,
        )

        member_list_response.additional_properties = d
        return member_list_response

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

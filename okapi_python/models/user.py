from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="User")


@_attrs_define
class User:
    """An OK user

    Attributes:
        id (int):  Example: 571234567890.
        name (str):  Example: Anna Petrova.
        first_name (str):  Example: Anna.
        last_name (str):  Example: Petrova.
        profile_url (str):  Example: https://ok.ru/profile/571234567890.
        photo_url (str | Unset):
    """

    id: int
    name: str
    first_name: str
    last_name: str
    profile_url: str
    photo_url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        first_name = self.first_name

        last_name = self.last_name

        profile_url = self.profile_url

        photo_url = self.photo_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "firstName": first_name,
                "lastName": last_name,
                "profileUrl": profile_url,
            }
        )
        if photo_url is not UNSET:
            field_dict["photoUrl"] = photo_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        first_name = d.pop("firstName")

        last_name = d.pop("lastName")

        profile_url = d.pop("profileUrl")

        photo_url = d.pop("photoUrl", UNSET)

        user = cls(
            id=id,
            name=name,
            first_name=first_name,
            last_name=last_name,
            profile_url=profile_url,
            photo_url=photo_url,
        )

        user.additional_properties = d
        return user

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

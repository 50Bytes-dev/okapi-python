from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Photo")


@_attrs_define
class Photo:
    """A photo of an album

    Attributes:
        photo_id (str): OK's photo id as digits Example: 1011458234641.
        album_id (str):  Example: 1011458223377.
        description (str): The photo's text, at most 4096 UTF-16 units Example: Dress, size 44.
        group_id (int | Unset):
        width (int | Unset):  Example: 1280.
        height (int | Unset):  Example: 960.
        url (str | Unset): The picture as OK serves it (a signed link)
        created_at (int | Unset): Unix ms Example: 1794500000000.
    """

    photo_id: str
    album_id: str
    description: str
    group_id: int | Unset = UNSET
    width: int | Unset = UNSET
    height: int | Unset = UNSET
    url: str | Unset = UNSET
    created_at: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        photo_id = self.photo_id

        album_id = self.album_id

        description = self.description

        group_id = self.group_id

        width = self.width

        height = self.height

        url = self.url

        created_at = self.created_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "photoId": photo_id,
                "albumId": album_id,
                "description": description,
            }
        )
        if group_id is not UNSET:
            field_dict["groupId"] = group_id
        if width is not UNSET:
            field_dict["width"] = width
        if height is not UNSET:
            field_dict["height"] = height
        if url is not UNSET:
            field_dict["url"] = url
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        photo_id = d.pop("photoId")

        album_id = d.pop("albumId")

        description = d.pop("description")

        group_id = d.pop("groupId", UNSET)

        width = d.pop("width", UNSET)

        height = d.pop("height", UNSET)

        url = d.pop("url", UNSET)

        created_at = d.pop("createdAt", UNSET)

        photo = cls(
            photo_id=photo_id,
            album_id=album_id,
            description=description,
            group_id=group_id,
            width=width,
            height=height,
            url=url,
            created_at=created_at,
        )

        photo.additional_properties = d
        return photo

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

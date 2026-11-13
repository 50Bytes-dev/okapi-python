from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.photo import Photo


T = TypeVar("T", bound="PhotoListResponse")


@_attrs_define
class PhotoListResponse:
    """
    Attributes:
        success (bool):
        photos (list[Photo]):
        total (int | Unset): Photos in the album, when OK tells it (a user's album)
        next_cursor (str | Unset): The next page; absent on the last
    """

    success: bool
    photos: list[Photo]
    total: int | Unset = UNSET
    next_cursor: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        photos = []
        for photos_item_data in self.photos:
            photos_item = photos_item_data.to_dict()
            photos.append(photos_item)

        total = self.total

        next_cursor = self.next_cursor

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "success": success,
                "photos": photos,
            }
        )
        if total is not UNSET:
            field_dict["total"] = total
        if next_cursor is not UNSET:
            field_dict["nextCursor"] = next_cursor

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.photo import Photo

        d = dict(src_dict)
        success = d.pop("success")

        photos = []
        _photos = d.pop("photos")
        for photos_item_data in _photos:
            photos_item = Photo.from_dict(photos_item_data)

            photos.append(photos_item)

        total = d.pop("total", UNSET)

        next_cursor = d.pop("nextCursor", UNSET)

        photo_list_response = cls(
            success=success,
            photos=photos,
            total=total,
            next_cursor=next_cursor,
        )

        photo_list_response.additional_properties = d
        return photo_list_response

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

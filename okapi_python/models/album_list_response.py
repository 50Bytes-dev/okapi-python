from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.album import Album


T = TypeVar("T", bound="AlbumListResponse")


@_attrs_define
class AlbumListResponse:
    """
    Attributes:
        success (bool):
        albums (list[Album]):
    """

    success: bool
    albums: list[Album]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        albums = []
        for albums_item_data in self.albums:
            albums_item = albums_item_data.to_dict()
            albums.append(albums_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "success": success,
                "albums": albums,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.album import Album

        d = dict(src_dict)
        success = d.pop("success")

        albums = []
        _albums = d.pop("albums")
        for albums_item_data in _albums:
            albums_item = Album.from_dict(albums_item_data)

            albums.append(albums_item)

        album_list_response = cls(
            success=success,
            albums=albums,
        )

        album_list_response.additional_properties = d
        return album_list_response

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

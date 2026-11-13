from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.album import Album


T = TypeVar("T", bound="AlbumResponse")


@_attrs_define
class AlbumResponse:
    """
    Attributes:
        success (bool):
        album (Album): A photo album of the account's OK user (no `groupId`) or of a group.
            The settings (`visibility`, `pinned`, `adminsOnly`) come only when they
            were read: OK's album lists carry none, so a list shows none; one album
            read by its id shows them (a group's only when OK shows the account the
            album's edit page, which it gives the group's administration).
    """

    success: bool
    album: Album
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        album = self.album.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "success": success,
                "album": album,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.album import Album

        d = dict(src_dict)
        success = d.pop("success")

        album = Album.from_dict(d.pop("album"))

        album_response = cls(
            success=success,
            album=album,
        )

        album_response.additional_properties = d
        return album_response

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

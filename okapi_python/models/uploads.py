from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.upload_counts import UploadCounts


T = TypeVar("T", bound="Uploads")


@_attrs_define
class Uploads:
    """The photos the gateway uploaded for the OK user lately, by every
    account of the user (OK's limits are the user's: 1000 new photos in
    5 minutes, 10000 a day). An upload that ended without an answer
    (`504 timeout`) counts too: OK may have taken it. Uploads from the
    user's other devices are not seen. Present while a login is stored.

        Attributes:
            album_photos (UploadCounts): Uploads in the last 5 minutes, hour and day, by the minute they were made
            media (UploadCounts): Uploads in the last 5 minutes, hour and day, by the minute they were made
    """

    album_photos: UploadCounts
    media: UploadCounts
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        album_photos = self.album_photos.to_dict()

        media = self.media.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "albumPhotos": album_photos,
                "media": media,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.upload_counts import UploadCounts

        d = dict(src_dict)
        album_photos = UploadCounts.from_dict(d.pop("albumPhotos"))

        media = UploadCounts.from_dict(d.pop("media"))

        uploads = cls(
            album_photos=album_photos,
            media=media,
        )

        uploads.additional_properties = d
        return uploads

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

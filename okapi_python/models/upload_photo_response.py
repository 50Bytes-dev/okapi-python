from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.photo import Photo


T = TypeVar("T", bound="UploadPhotoResponse")


@_attrs_define
class UploadPhotoResponse:
    """
    Attributes:
        success (bool):
        photo (Photo): A photo of an album
        duplicate (bool): The `ref` was uploaded before; this is that photo, nothing was uploaded now
    """

    success: bool
    photo: Photo
    duplicate: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        photo = self.photo.to_dict()

        duplicate = self.duplicate

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "success": success,
                "photo": photo,
                "duplicate": duplicate,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.photo import Photo

        d = dict(src_dict)
        success = d.pop("success")

        photo = Photo.from_dict(d.pop("photo"))

        duplicate = d.pop("duplicate")

        upload_photo_response = cls(
            success=success,
            photo=photo,
            duplicate=duplicate,
        )

        upload_photo_response.additional_properties = d
        return upload_photo_response

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

from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UploadAlbumPhotoRequest")


@_attrs_define
class UploadAlbumPhotoRequest:
    """Exactly one of `url` and `data`

    Attributes:
        url (str | Unset): An http(s) URL the gateway fetches Example: https://example.com/photo.jpg.
        data (str | Unset): The photo as base64 or a base64 data URL
        description (str | Unset): The photo's text, at most 4096 UTF-16 units Example: Dress, size 44.
        ref (str | Unset): Your idempotency key, at most 128 bytes; a repeat never uploads a second photo Example:
            order-1042/photo-1.
    """

    url: str | Unset = UNSET
    data: str | Unset = UNSET
    description: str | Unset = UNSET
    ref: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        url = self.url

        data = self.data

        description = self.description

        ref = self.ref

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if url is not UNSET:
            field_dict["url"] = url
        if data is not UNSET:
            field_dict["data"] = data
        if description is not UNSET:
            field_dict["description"] = description
        if ref is not UNSET:
            field_dict["ref"] = ref

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        url = d.pop("url", UNSET)

        data = d.pop("data", UNSET)

        description = d.pop("description", UNSET)

        ref = d.pop("ref", UNSET)

        upload_album_photo_request = cls(
            url=url,
            data=data,
            description=description,
            ref=ref,
        )

        upload_album_photo_request.additional_properties = d
        return upload_album_photo_request

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

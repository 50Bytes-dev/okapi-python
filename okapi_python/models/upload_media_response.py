from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="UploadMediaResponse")


@_attrs_define
class UploadMediaResponse:
    """
    Attributes:
        success (bool):
        attachment (str): The handle for `POST /messages` (`okph2.…`), valid in any chat of the same OK user until
            `expiresAt` Example: okph2.eyJwIjoi….
        expires_at (int): Unix seconds from which a send refuses the handle (`attachment_rejected`) without calling OK;
            `OKAPI_MEDIA_HANDLE_TTL` (24 h) after the upload Example: 1794586400.
        width (int): Pixels of the photo as uploaded Example: 1280.
        height (int):  Example: 960.
        size (int): Bytes uploaded Example: 183402.
    """

    success: bool
    attachment: str
    expires_at: int
    width: int
    height: int
    size: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        attachment = self.attachment

        expires_at = self.expires_at

        width = self.width

        height = self.height

        size = self.size

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "success": success,
                "attachment": attachment,
                "expiresAt": expires_at,
                "width": width,
                "height": height,
                "size": size,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        success = d.pop("success")

        attachment = d.pop("attachment")

        expires_at = d.pop("expiresAt")

        width = d.pop("width")

        height = d.pop("height")

        size = d.pop("size")

        upload_media_response = cls(
            success=success,
            attachment=attachment,
            expires_at=expires_at,
            width=width,
            height=height,
            size=size,
        )

        upload_media_response.additional_properties = d
        return upload_media_response

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

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
        attachment (str): The handle for `POST /messages` (`okph1.…`), valid in any chat of the same OK user Example:
            okph1.eyJwIjoi….
        width (int): Pixels of the photo as uploaded Example: 1280.
        height (int):  Example: 960.
        size (int): Bytes uploaded Example: 183402.
    """

    success: bool
    attachment: str
    width: int
    height: int
    size: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        attachment = self.attachment

        width = self.width

        height = self.height

        size = self.size

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "success": success,
                "attachment": attachment,
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

        width = d.pop("width")

        height = d.pop("height")

        size = d.pop("size")

        upload_media_response = cls(
            success=success,
            attachment=attachment,
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

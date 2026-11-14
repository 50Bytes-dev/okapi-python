from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.delete_photo_result_status import DeletePhotoResultStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="DeletePhotoResult")


@_attrs_define
class DeletePhotoResult:
    """
    Attributes:
        photo_id (str):
        status (DeletePhotoResultStatus): `deleted`; `not_found` (OK found nothing to delete);
            `forbidden` (OK refused the right); `failed` (`code` says how, as
            the photo's own delete would answer); `skipped` (not tried:
            `code` says why: `paused`, `not_logged_in`, `not_connected`, or
            `timeout` when the request's time ran out)
        code (str | Unset): The error code of a `failed` or `skipped` photo Example: timeout.
        upstream_code (str | Unset): OK's code, when it gave one
    """

    photo_id: str
    status: DeletePhotoResultStatus
    code: str | Unset = UNSET
    upstream_code: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        photo_id = self.photo_id

        status = self.status.value

        code = self.code

        upstream_code = self.upstream_code

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "photoId": photo_id,
                "status": status,
            }
        )
        if code is not UNSET:
            field_dict["code"] = code
        if upstream_code is not UNSET:
            field_dict["upstreamCode"] = upstream_code

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        photo_id = d.pop("photoId")

        status = DeletePhotoResultStatus(d.pop("status"))

        code = d.pop("code", UNSET)

        upstream_code = d.pop("upstreamCode", UNSET)

        delete_photo_result = cls(
            photo_id=photo_id,
            status=status,
            code=code,
            upstream_code=upstream_code,
        )

        delete_photo_result.additional_properties = d
        return delete_photo_result

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

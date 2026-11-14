from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="UploadCounts")


@_attrs_define
class UploadCounts:
    """Uploads in the last 5 minutes, hour and day, by the minute they were made

    Attributes:
        last_5_minutes (int):  Example: 3.
        last_hour (int):  Example: 120.
        last_day (int):  Example: 2400.
    """

    last_5_minutes: int
    last_hour: int
    last_day: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        last_5_minutes = self.last_5_minutes

        last_hour = self.last_hour

        last_day = self.last_day

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "last5Minutes": last_5_minutes,
                "lastHour": last_hour,
                "lastDay": last_day,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        last_5_minutes = d.pop("last5Minutes")

        last_hour = d.pop("lastHour")

        last_day = d.pop("lastDay")

        upload_counts = cls(
            last_5_minutes=last_5_minutes,
            last_hour=last_hour,
            last_day=last_day,
        )

        upload_counts.additional_properties = d
        return upload_counts

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

from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.pause_reason import PauseReason

T = TypeVar("T", bound="Pause")


@_attrs_define
class Pause:
    """The pause of the OK user. `reason`: `spam` (OK's antispam or flood
    refusal), `restricted` (OK restricted sending). Lifted only by
    `POST /session/resume`.

        Attributes:
            reason (PauseReason):
            upstream_code (str): The OK error that paused it
            since (int): Unix time in seconds Example: 1794500000.
    """

    reason: PauseReason
    upstream_code: str
    since: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        reason = self.reason.value

        upstream_code = self.upstream_code

        since = self.since

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "reason": reason,
                "upstreamCode": upstream_code,
                "since": since,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        reason = PauseReason(d.pop("reason"))

        upstream_code = d.pop("upstreamCode")

        since = d.pop("since")

        pause = cls(
            reason=reason,
            upstream_code=upstream_code,
            since=since,
        )

        pause.additional_properties = d
        return pause

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

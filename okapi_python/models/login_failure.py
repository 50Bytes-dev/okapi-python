from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.login_failure_reason import LoginFailureReason
from ..types import UNSET, Unset

T = TypeVar("T", bound="LoginFailure")


@_attrs_define
class LoginFailure:
    """Step `failed`. `reason`: `expired` (`OKAPI_LOGIN_TIMEOUT`, or OK
    expired the QR and gave no new one), `cancelled` (a new login, a
    disconnect or `DELETE /session/login`), `unavailable` (ok.ru gave no
    QR), `verification_required` (OK asks the user to confirm the login
    on a device), `failed` (anything else; `upstreamCode`).

        Attributes:
            reason (LoginFailureReason):
            upstream_code (str | Unset):
    """

    reason: LoginFailureReason
    upstream_code: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        reason = self.reason.value

        upstream_code = self.upstream_code

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "reason": reason,
            }
        )
        if upstream_code is not UNSET:
            field_dict["upstreamCode"] = upstream_code

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        reason = LoginFailureReason(d.pop("reason"))

        upstream_code = d.pop("upstreamCode", UNSET)

        login_failure = cls(
            reason=reason,
            upstream_code=upstream_code,
        )

        login_failure.additional_properties = d
        return login_failure

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

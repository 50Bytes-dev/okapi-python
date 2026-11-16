from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.login import Login


T = TypeVar("T", bound="LoginResponse")


@_attrs_define
class LoginResponse:
    """
    Attributes:
        success (bool):
        login (Login): The login into OK. `step`: `none` (no login ran), `qr` (scan `qr`
            and confirm in the OK app), `code` (the profile has OK's two-factor
            protection: give the SMS code, `sms`), `done` (`okUser`;
            `Connected` follows), `failed` (`failure`).
    """

    success: bool
    login: Login
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        login = self.login.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "success": success,
                "login": login,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.login import Login

        d = dict(src_dict)
        success = d.pop("success")

        login = Login.from_dict(d.pop("login"))

        login_response = cls(
            success=success,
            login=login,
        )

        login_response.additional_properties = d
        return login_response

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

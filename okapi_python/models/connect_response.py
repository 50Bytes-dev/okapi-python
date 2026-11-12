from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.ok_user import OkUser


T = TypeVar("T", bound="ConnectResponse")


@_attrs_define
class ConnectResponse:
    """
    Attributes:
        success (bool):
        connected (bool): false when the session did not connect within 10 s; it goes on connecting
        ok_user (OkUser): The OK user the account is logged into
    """

    success: bool
    connected: bool
    ok_user: OkUser
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        connected = self.connected

        ok_user = self.ok_user.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "success": success,
                "connected": connected,
                "okUser": ok_user,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ok_user import OkUser

        d = dict(src_dict)
        success = d.pop("success")

        connected = d.pop("connected")

        ok_user = OkUser.from_dict(d.pop("okUser"))

        connect_response = cls(
            success=success,
            connected=connected,
            ok_user=ok_user,
        )

        connect_response.additional_properties = d
        return connect_response

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

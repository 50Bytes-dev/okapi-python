from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.health_response_status import HealthResponseStatus

T = TypeVar("T", bound="HealthResponse")


@_attrs_define
class HealthResponse:
    """
    Attributes:
        success (bool): false when the database does not answer Example: True.
        status (HealthResponseStatus): `degraded` when the database does not answer
        version (str):  Example: 0.1.1.
        uptime_seconds (int):  Example: 12345.
        db (bool): Whether the database answers a ping Example: True.
        accounts (int): Accounts of the gateway Example: 4.
        connected (int): Accounts with a connected messenger session Example: 3.
    """

    success: bool
    status: HealthResponseStatus
    version: str
    uptime_seconds: int
    db: bool
    accounts: int
    connected: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        status = self.status.value

        version = self.version

        uptime_seconds = self.uptime_seconds

        db = self.db

        accounts = self.accounts

        connected = self.connected

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "success": success,
                "status": status,
                "version": version,
                "uptimeSeconds": uptime_seconds,
                "db": db,
                "accounts": accounts,
                "connected": connected,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        success = d.pop("success")

        status = HealthResponseStatus(d.pop("status"))

        version = d.pop("version")

        uptime_seconds = d.pop("uptimeSeconds")

        db = d.pop("db")

        accounts = d.pop("accounts")

        connected = d.pop("connected")

        health_response = cls(
            success=success,
            status=status,
            version=version,
            uptime_seconds=uptime_seconds,
            db=db,
            accounts=accounts,
            connected=connected,
        )

        health_response.additional_properties = d
        return health_response

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

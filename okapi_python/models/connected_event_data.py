from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.ok_user import OkUser


T = TypeVar("T", bound="ConnectedEventData")


@_attrs_define
class ConnectedEventData:
    """
    Attributes:
        ok_user (OkUser): The OK user the account is logged into
        reconnect (bool): The connection came back after an outage
    """

    ok_user: OkUser
    reconnect: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ok_user = self.ok_user.to_dict()

        reconnect = self.reconnect

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "okUser": ok_user,
                "reconnect": reconnect,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ok_user import OkUser

        d = dict(src_dict)
        ok_user = OkUser.from_dict(d.pop("okUser"))

        reconnect = d.pop("reconnect")

        connected_event_data = cls(
            ok_user=ok_user,
            reconnect=reconnect,
        )

        connected_event_data.additional_properties = d
        return connected_event_data

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

from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="EventEnvelope")


@_attrs_define
class EventEnvelope:
    """The fields of every event; `data` depends on `type`.

    Attributes:
        id (UUID): The event id, the same on every retry; dedupe by it
        type_ (Any):
        account_id (UUID):
        account_name (str):
        timestamp (int): Unix time in seconds of the event Example: 1794500000.
        data (Any):
    """

    id: UUID
    type_: Any
    account_id: UUID
    account_name: str
    timestamp: int
    data: Any
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        type_ = self.type_

        account_id = str(self.account_id)

        account_name = self.account_name

        timestamp = self.timestamp

        data = self.data

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "type": type_,
                "accountId": account_id,
                "accountName": account_name,
                "timestamp": timestamp,
                "data": data,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        type_ = d.pop("type")

        account_id = UUID(d.pop("accountId"))

        account_name = d.pop("accountName")

        timestamp = d.pop("timestamp")

        data = d.pop("data")

        event_envelope = cls(
            id=id,
            type_=type_,
            account_id=account_id,
            account_name=account_name,
            timestamp=timestamp,
            data=data,
        )

        event_envelope.additional_properties = d
        return event_envelope

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

from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="LoginSms")


@_attrs_define
class LoginSms:
    """Step `code`: OK's two-factor protection sent a code by SMS. Give it
    with `POST /session/login/code`; have OK deliver it again with
    `POST /session/login/code/resend`.

        Attributes:
            sent_at (int): Unix time in seconds when the gateway last asked OK for the code (the send or a resend) Example:
                1794500030.
            resend_at (int): Unix time in seconds from when OK takes a resend (its code page's timer, 60 s) Example:
                1794500090.
            sent_to (str | Unset): The number the SMS went to, masked as OK shows it; absent when OK showed none Example:
                +7********12.
            resends (int | Unset): How many resends OK took; absent when none Example: 1.
            wrong_codes (int | Unset): How many codes OK did not take; absent when none Example: 1.
    """

    sent_at: int
    resend_at: int
    sent_to: str | Unset = UNSET
    resends: int | Unset = UNSET
    wrong_codes: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        sent_at = self.sent_at

        resend_at = self.resend_at

        sent_to = self.sent_to

        resends = self.resends

        wrong_codes = self.wrong_codes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "sentAt": sent_at,
                "resendAt": resend_at,
            }
        )
        if sent_to is not UNSET:
            field_dict["sentTo"] = sent_to
        if resends is not UNSET:
            field_dict["resends"] = resends
        if wrong_codes is not UNSET:
            field_dict["wrongCodes"] = wrong_codes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        sent_at = d.pop("sentAt")

        resend_at = d.pop("resendAt")

        sent_to = d.pop("sentTo", UNSET)

        resends = d.pop("resends", UNSET)

        wrong_codes = d.pop("wrongCodes", UNSET)

        login_sms = cls(
            sent_at=sent_at,
            resend_at=resend_at,
            sent_to=sent_to,
            resends=resends,
            wrong_codes=wrong_codes,
        )

        login_sms.additional_properties = d
        return login_sms

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

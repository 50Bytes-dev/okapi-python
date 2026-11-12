from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="LoginQr")


@_attrs_define
class LoginQr:
    """Step `qr`: the account's own login QR from ok.ru. Scan it with the
    OK app and confirm only if the app shows `code`.

        Attributes:
            image (str): The QR as a PNG data URL Example: data:image/png;base64,iVBORw0KGgo….
            link (str): The link the QR holds Example: https://ok.ru/qrCode/<token>.
            code (str): The 4-digit code the OK app shows after the scan; it must match Example: 1345.
    """

    image: str
    link: str
    code: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        image = self.image

        link = self.link

        code = self.code

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "image": image,
                "link": link,
                "code": code,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        image = d.pop("image")

        link = d.pop("link")

        code = d.pop("code")

        login_qr = cls(
            image=image,
            link=link,
            code=code,
        )

        login_qr.additional_properties = d
        return login_qr

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

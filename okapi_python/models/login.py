from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.login_step import LoginStep
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.login_failure import LoginFailure
    from ..models.login_qr import LoginQr
    from ..models.ok_user import OkUser


T = TypeVar("T", bound="Login")


@_attrs_define
class Login:
    """The login into OK. `step`: `none` (no login ran), `qr` (scan `qr`
    and confirm in the OK app), `done` (`okUser`; `Connected` follows),
    `failed` (`failure`).

        Attributes:
            step (LoginStep):
            started_at (int | Unset): Unix time in seconds
            expires_at (int | Unset): Unix time in seconds when the login fails `expired` (`OKAPI_LOGIN_TIMEOUT` after the
                start)
            qr (LoginQr | Unset): Step `qr`: the account's own login QR from ok.ru. Scan it with the
                OK app and confirm only if the app shows `code`.
            ok_user (OkUser | Unset): The OK user the account is logged into
            failure (LoginFailure | Unset): Step `failed`. `reason`: `expired` (`OKAPI_LOGIN_TIMEOUT`, or OK
                expired the QR and gave no new one), `cancelled` (a new login, a
                disconnect or `DELETE /session/login`), `unavailable` (ok.ru gave no
                QR), `verification_required` (OK asks the user to confirm the login
                on a device), `failed` (anything else; `upstreamCode`).
    """

    step: LoginStep
    started_at: int | Unset = UNSET
    expires_at: int | Unset = UNSET
    qr: LoginQr | Unset = UNSET
    ok_user: OkUser | Unset = UNSET
    failure: LoginFailure | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        step = self.step.value

        started_at = self.started_at

        expires_at = self.expires_at

        qr: dict[str, Any] | Unset = UNSET
        if not isinstance(self.qr, Unset):
            qr = self.qr.to_dict()

        ok_user: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ok_user, Unset):
            ok_user = self.ok_user.to_dict()

        failure: dict[str, Any] | Unset = UNSET
        if not isinstance(self.failure, Unset):
            failure = self.failure.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "step": step,
            }
        )
        if started_at is not UNSET:
            field_dict["startedAt"] = started_at
        if expires_at is not UNSET:
            field_dict["expiresAt"] = expires_at
        if qr is not UNSET:
            field_dict["qr"] = qr
        if ok_user is not UNSET:
            field_dict["okUser"] = ok_user
        if failure is not UNSET:
            field_dict["failure"] = failure

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.login_failure import LoginFailure
        from ..models.login_qr import LoginQr
        from ..models.ok_user import OkUser

        d = dict(src_dict)
        step = LoginStep(d.pop("step"))

        started_at = d.pop("startedAt", UNSET)

        expires_at = d.pop("expiresAt", UNSET)

        _qr = d.pop("qr", UNSET)
        qr: LoginQr | Unset
        if isinstance(_qr, Unset):
            qr = UNSET
        else:
            qr = LoginQr.from_dict(_qr)

        _ok_user = d.pop("okUser", UNSET)
        ok_user: OkUser | Unset
        if isinstance(_ok_user, Unset):
            ok_user = UNSET
        else:
            ok_user = OkUser.from_dict(_ok_user)

        _failure = d.pop("failure", UNSET)
        failure: LoginFailure | Unset
        if isinstance(_failure, Unset):
            failure = UNSET
        else:
            failure = LoginFailure.from_dict(_failure)

        login = cls(
            step=step,
            started_at=started_at,
            expires_at=expires_at,
            qr=qr,
            ok_user=ok_user,
            failure=failure,
        )

        login.additional_properties = d
        return login

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

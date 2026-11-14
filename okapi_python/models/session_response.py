from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.login import Login
    from ..models.ok_user import OkUser
    from ..models.pause import Pause
    from ..models.uploads import Uploads


T = TypeVar("T", bound="SessionResponse")


@_attrs_define
class SessionResponse:
    """
    Attributes:
        success (bool):
        logged_in (bool): An OK login is stored
        connected (bool): The messenger session is connected
        ok_user (OkUser | Unset): The OK user the account is logged into
        login (Login | Unset): The login into OK. `step`: `none` (no login ran), `qr` (scan `qr`
            and confirm in the OK app), `done` (`okUser`; `Connected` follows),
            `failed` (`failure`).
        pause (Pause | Unset): The pause of the OK user. `reason`: `spam` (OK's antispam or flood
            refusal), `restricted` (OK restricted sending), `captcha` (ok.ru sent a
            request to its captcha: pass it in a browser of the user, then
            resume; `upstreamCode` is empty). Lifted only by
            `POST /session/resume`.
        uploads (Uploads | Unset): The photos the gateway uploaded for the OK user lately, by every
            account of the user (OK's limits are the user's: 1000 new photos in
            5 minutes, 10000 a day). An upload that ended without an answer
            (`504 timeout`) counts too: OK may have taken it. Uploads from the
            user's other devices are not seen. Present while a login is stored.
    """

    success: bool
    logged_in: bool
    connected: bool
    ok_user: OkUser | Unset = UNSET
    login: Login | Unset = UNSET
    pause: Pause | Unset = UNSET
    uploads: Uploads | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        logged_in = self.logged_in

        connected = self.connected

        ok_user: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ok_user, Unset):
            ok_user = self.ok_user.to_dict()

        login: dict[str, Any] | Unset = UNSET
        if not isinstance(self.login, Unset):
            login = self.login.to_dict()

        pause: dict[str, Any] | Unset = UNSET
        if not isinstance(self.pause, Unset):
            pause = self.pause.to_dict()

        uploads: dict[str, Any] | Unset = UNSET
        if not isinstance(self.uploads, Unset):
            uploads = self.uploads.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "success": success,
                "loggedIn": logged_in,
                "connected": connected,
            }
        )
        if ok_user is not UNSET:
            field_dict["okUser"] = ok_user
        if login is not UNSET:
            field_dict["login"] = login
        if pause is not UNSET:
            field_dict["pause"] = pause
        if uploads is not UNSET:
            field_dict["uploads"] = uploads

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.login import Login
        from ..models.ok_user import OkUser
        from ..models.pause import Pause
        from ..models.uploads import Uploads

        d = dict(src_dict)
        success = d.pop("success")

        logged_in = d.pop("loggedIn")

        connected = d.pop("connected")

        _ok_user = d.pop("okUser", UNSET)
        ok_user: OkUser | Unset
        if isinstance(_ok_user, Unset):
            ok_user = UNSET
        else:
            ok_user = OkUser.from_dict(_ok_user)

        _login = d.pop("login", UNSET)
        login: Login | Unset
        if isinstance(_login, Unset):
            login = UNSET
        else:
            login = Login.from_dict(_login)

        _pause = d.pop("pause", UNSET)
        pause: Pause | Unset
        if isinstance(_pause, Unset):
            pause = UNSET
        else:
            pause = Pause.from_dict(_pause)

        _uploads = d.pop("uploads", UNSET)
        uploads: Uploads | Unset
        if isinstance(_uploads, Unset):
            uploads = UNSET
        else:
            uploads = Uploads.from_dict(_uploads)

        session_response = cls(
            success=success,
            logged_in=logged_in,
            connected=connected,
            ok_user=ok_user,
            login=login,
            pause=pause,
            uploads=uploads,
        )

        session_response.additional_properties = d
        return session_response

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

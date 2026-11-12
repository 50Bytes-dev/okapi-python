from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pause import Pause


T = TypeVar("T", bound="ErrorResponse")


@_attrs_define
class ErrorResponse:
    """The body of every error. Branch on `code`; the details below come with the codes that name them.

    Attributes:
        success (bool):
        code (str): The machine code (see "Codes" above) Example: write_forbidden.
        error (str): A fixed English text per case; never OK's text. Do not branch on it. Example: The chat does not let
            this account write.
        upstream_code (str | Unset): OK's error string as OK gave it Example: chat.denied.
        pause (Pause | Unset): The pause of the OK user. `reason`: `spam` (OK's antispam or flood
            refusal), `restricted` (OK restricted sending). Lifted only by
            `POST /session/resume`.
        rejected_attachments (list[int] | Unset): `attachment_rejected`: the indexes of the unusable attachments
            Example: [1].
        retry_after_ms (int | Unset): When the call may come again, in milliseconds (`upload_failed` while the gateway
            is busy with other photos) Example: 1000.
    """

    success: bool
    code: str
    error: str
    upstream_code: str | Unset = UNSET
    pause: Pause | Unset = UNSET
    rejected_attachments: list[int] | Unset = UNSET
    retry_after_ms: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        code = self.code

        error = self.error

        upstream_code = self.upstream_code

        pause: dict[str, Any] | Unset = UNSET
        if not isinstance(self.pause, Unset):
            pause = self.pause.to_dict()

        rejected_attachments: list[int] | Unset = UNSET
        if not isinstance(self.rejected_attachments, Unset):
            rejected_attachments = self.rejected_attachments

        retry_after_ms = self.retry_after_ms

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "success": success,
                "code": code,
                "error": error,
            }
        )
        if upstream_code is not UNSET:
            field_dict["upstreamCode"] = upstream_code
        if pause is not UNSET:
            field_dict["pause"] = pause
        if rejected_attachments is not UNSET:
            field_dict["rejectedAttachments"] = rejected_attachments
        if retry_after_ms is not UNSET:
            field_dict["retryAfterMs"] = retry_after_ms

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pause import Pause

        d = dict(src_dict)
        success = d.pop("success")

        code = d.pop("code")

        error = d.pop("error")

        upstream_code = d.pop("upstreamCode", UNSET)

        _pause = d.pop("pause", UNSET)
        pause: Pause | Unset
        if isinstance(_pause, Unset):
            pause = UNSET
        else:
            pause = Pause.from_dict(_pause)

        rejected_attachments = cast(list[int], d.pop("rejectedAttachments", UNSET))

        retry_after_ms = d.pop("retryAfterMs", UNSET)

        error_response = cls(
            success=success,
            code=code,
            error=error,
            upstream_code=upstream_code,
            pause=pause,
            rejected_attachments=rejected_attachments,
            retry_after_ms=retry_after_ms,
        )

        error_response.additional_properties = d
        return error_response

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

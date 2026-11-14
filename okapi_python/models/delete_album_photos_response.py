from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.delete_photo_result import DeletePhotoResult
    from ..models.pause import Pause


T = TypeVar("T", bound="DeleteAlbumPhotosResponse")


@_attrs_define
class DeleteAlbumPhotosResponse:
    """
    Attributes:
        success (bool):
        results (list[DeletePhotoResult]): One per photo, in the order first asked
        pause (Pause | Unset): The pause of the OK user. `reason`: `spam` (OK's antispam or flood
            refusal), `restricted` (OK restricted sending), `captcha` (ok.ru sent a
            request to its captcha: pass it in a browser of the user, then
            resume; `upstreamCode` is empty). Lifted only by
            `POST /session/resume`.
    """

    success: bool
    results: list[DeletePhotoResult]
    pause: Pause | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        results = []
        for results_item_data in self.results:
            results_item = results_item_data.to_dict()
            results.append(results_item)

        pause: dict[str, Any] | Unset = UNSET
        if not isinstance(self.pause, Unset):
            pause = self.pause.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "success": success,
                "results": results,
            }
        )
        if pause is not UNSET:
            field_dict["pause"] = pause

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.delete_photo_result import DeletePhotoResult
        from ..models.pause import Pause

        d = dict(src_dict)
        success = d.pop("success")

        results = []
        _results = d.pop("results")
        for results_item_data in _results:
            results_item = DeletePhotoResult.from_dict(results_item_data)

            results.append(results_item)

        _pause = d.pop("pause", UNSET)
        pause: Pause | Unset
        if isinstance(_pause, Unset):
            pause = UNSET
        else:
            pause = Pause.from_dict(_pause)

        delete_album_photos_response = cls(
            success=success,
            results=results,
            pause=pause,
        )

        delete_album_photos_response.additional_properties = d
        return delete_album_photos_response

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

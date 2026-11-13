from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.album_visibility import AlbumVisibility
from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateAlbumRequest")


@_attrs_define
class UpdateAlbumRequest:
    """The fields to change, at least one

    Attributes:
        title (str | Unset): At most 256 UTF-16 units, not blank
        visibility (list[AlbumVisibility] | Unset):
    """

    title: str | Unset = UNSET
    visibility: list[AlbumVisibility] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        title = self.title

        visibility: list[str] | Unset = UNSET
        if not isinstance(self.visibility, Unset):
            visibility = []
            for visibility_item_data in self.visibility:
                visibility_item = visibility_item_data.value
                visibility.append(visibility_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if title is not UNSET:
            field_dict["title"] = title
        if visibility is not UNSET:
            field_dict["visibility"] = visibility

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        title = d.pop("title", UNSET)

        _visibility = d.pop("visibility", UNSET)
        visibility: list[AlbumVisibility] | Unset = UNSET
        if _visibility is not UNSET:
            visibility = []
            for visibility_item_data in _visibility:
                visibility_item = AlbumVisibility(visibility_item_data)

                visibility.append(visibility_item)

        update_album_request = cls(
            title=title,
            visibility=visibility,
        )

        update_album_request.additional_properties = d
        return update_album_request

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

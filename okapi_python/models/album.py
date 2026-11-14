from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.album_visibility import AlbumVisibility
from ..types import UNSET, Unset

T = TypeVar("T", bound="Album")


@_attrs_define
class Album:
    """A photo album of the account's OK user (no `groupId`) or of a group.
    The settings (`visibility`, `pinned`, `adminsOnly`) come only when they
    were read: OK's album lists carry none, so a list shows none; one album
    read by its id shows them (a group's only when OK shows the account the
    album's edit page, which it gives the group's administration).

        Attributes:
            album_id (str): OK's album id as digits, or `personal` Example: 1011458223377.
            title (str):  Example: Spring collection.
            can_upload (bool): The account may upload into the album: always into the user's
                own; into a group's, as OK's list of the group's albums tells it
                (a moderator everywhere, a member where the album is open to
                members)
            group_id (int | Unset): The group of a group's album Example: 70000060985873.
            photos_count (int | Unset): Photos in the album, when OK tells it Example: 12.
            visibility (list[AlbumVisibility] | Unset): Who sees a user's album (not the personal one's); not in a list
                Example: ['public'].
            pinned (bool | Unset): A group's album is shown first; not in a list
            admins_only (bool | Unset): Only the group's administration adds photos to a group's album; not in a list
            personal (bool | Unset): The user's "Личные фотографии", which has no id on OK, no settings here and no
                `photosCount` (OK does not give it)
    """

    album_id: str
    title: str
    can_upload: bool
    group_id: int | Unset = UNSET
    photos_count: int | Unset = UNSET
    visibility: list[AlbumVisibility] | Unset = UNSET
    pinned: bool | Unset = UNSET
    admins_only: bool | Unset = UNSET
    personal: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        album_id = self.album_id

        title = self.title

        can_upload = self.can_upload

        group_id = self.group_id

        photos_count = self.photos_count

        visibility: list[str] | Unset = UNSET
        if not isinstance(self.visibility, Unset):
            visibility = []
            for visibility_item_data in self.visibility:
                visibility_item = visibility_item_data.value
                visibility.append(visibility_item)

        pinned = self.pinned

        admins_only = self.admins_only

        personal = self.personal

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "albumId": album_id,
                "title": title,
                "canUpload": can_upload,
            }
        )
        if group_id is not UNSET:
            field_dict["groupId"] = group_id
        if photos_count is not UNSET:
            field_dict["photosCount"] = photos_count
        if visibility is not UNSET:
            field_dict["visibility"] = visibility
        if pinned is not UNSET:
            field_dict["pinned"] = pinned
        if admins_only is not UNSET:
            field_dict["adminsOnly"] = admins_only
        if personal is not UNSET:
            field_dict["personal"] = personal

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        album_id = d.pop("albumId")

        title = d.pop("title")

        can_upload = d.pop("canUpload")

        group_id = d.pop("groupId", UNSET)

        photos_count = d.pop("photosCount", UNSET)

        _visibility = d.pop("visibility", UNSET)
        visibility: list[AlbumVisibility] | Unset = UNSET
        if _visibility is not UNSET:
            visibility = []
            for visibility_item_data in _visibility:
                visibility_item = AlbumVisibility(visibility_item_data)

                visibility.append(visibility_item)

        pinned = d.pop("pinned", UNSET)

        admins_only = d.pop("adminsOnly", UNSET)

        personal = d.pop("personal", UNSET)

        album = cls(
            album_id=album_id,
            title=title,
            can_upload=can_upload,
            group_id=group_id,
            photos_count=photos_count,
            visibility=visibility,
            pinned=pinned,
            admins_only=admins_only,
            personal=personal,
        )

        album.additional_properties = d
        return album

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

from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.message_attachment_type import MessageAttachmentType
from ..types import UNSET, Unset

T = TypeVar("T", bound="MessageAttachment")


@_attrs_define
class MessageAttachment:
    """
    Attributes:
        type_ (MessageAttachmentType):
        photo_id (int | Unset): `photo`: OK's photo id
        url (str | Unset): A link to the content, when OK gives one
        width (int | Unset):
        height (int | Unset):
    """

    type_: MessageAttachmentType
    photo_id: int | Unset = UNSET
    url: str | Unset = UNSET
    width: int | Unset = UNSET
    height: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        photo_id = self.photo_id

        url = self.url

        width = self.width

        height = self.height

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
            }
        )
        if photo_id is not UNSET:
            field_dict["photoId"] = photo_id
        if url is not UNSET:
            field_dict["url"] = url
        if width is not UNSET:
            field_dict["width"] = width
        if height is not UNSET:
            field_dict["height"] = height

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = MessageAttachmentType(d.pop("type"))

        photo_id = d.pop("photoId", UNSET)

        url = d.pop("url", UNSET)

        width = d.pop("width", UNSET)

        height = d.pop("height", UNSET)

        message_attachment = cls(
            type_=type_,
            photo_id=photo_id,
            url=url,
            width=width,
            height=height,
        )

        message_attachment.additional_properties = d
        return message_attachment

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

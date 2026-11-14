from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.chat_cant_write_reason import ChatCantWriteReason
from ..models.chat_status import ChatStatus
from ..models.chat_type import ChatType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.message import Message


T = TypeVar("T", bound="Chat")


@_attrs_define
class Chat:
    """A chat of the account. `canWrite` is read from the chat as OK lists
    it, by the rules of OK's web client: a chat that is not a dialog and
    is not active, restrictions on input, a group chat whose members OK
    listed in full without the account, a channel the account is neither
    the owner nor a posting admin of. The other side of a dialog may
    still refuse a send (`write_forbidden`).

        Attributes:
            chat_id (int):  Example: -123456789012345.
            type_ (ChatType): `user` (dialog with a person), `self` (dialog with oneself), `chat` (group chat), `group`
                (chat with an OK group), `channel`
            title (str): The chat's title; for a dialog, the other person's name Example: Test Group chat.
            status (ChatStatus): `active`; `left` (the account left it), `removed` (deleted),
                `closed` (closed by its owner), `blocked` (blocked by OK, a
                blocked group's chat among them). OK's statuses; only `active` is
                seen live.
            can_write (bool): The account may write in the chat, as the chat tells
            last_event_at (int): Unix time in milliseconds of the chat's last event Example: 1794500000000.
            user_id (int | Unset): `user`: the other person
            group_id (int | Unset): `group`: the OK group the chat is with, when OK names it Example: 70000060985873.
            owner_id (int | Unset): The chat's owner, when OK names one
            members_count (int | Unset): Members, when OK counts them Example: 3.
            cant_write_reason (ChatCantWriteReason | Unset): Why not, when `canWrite` is false: `inactive` (the chat is not
                active: see `status`), `restricted` (OK restricts writing here),
                `not_member` (the account is not a member), `not_admin` (a
                channel: only its owner and admins post)
            last_message (Message | Unset): A message. Its text is the sender's: treat it as untrusted.
                `status` is `edited` or `removed` when OK marks it so.
    """

    chat_id: int
    type_: ChatType
    title: str
    status: ChatStatus
    can_write: bool
    last_event_at: int
    user_id: int | Unset = UNSET
    group_id: int | Unset = UNSET
    owner_id: int | Unset = UNSET
    members_count: int | Unset = UNSET
    cant_write_reason: ChatCantWriteReason | Unset = UNSET
    last_message: Message | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        chat_id = self.chat_id

        type_ = self.type_.value

        title = self.title

        status = self.status.value

        can_write = self.can_write

        last_event_at = self.last_event_at

        user_id = self.user_id

        group_id = self.group_id

        owner_id = self.owner_id

        members_count = self.members_count

        cant_write_reason: str | Unset = UNSET
        if not isinstance(self.cant_write_reason, Unset):
            cant_write_reason = self.cant_write_reason.value

        last_message: dict[str, Any] | Unset = UNSET
        if not isinstance(self.last_message, Unset):
            last_message = self.last_message.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "chatId": chat_id,
                "type": type_,
                "title": title,
                "status": status,
                "canWrite": can_write,
                "lastEventAt": last_event_at,
            }
        )
        if user_id is not UNSET:
            field_dict["userId"] = user_id
        if group_id is not UNSET:
            field_dict["groupId"] = group_id
        if owner_id is not UNSET:
            field_dict["ownerId"] = owner_id
        if members_count is not UNSET:
            field_dict["membersCount"] = members_count
        if cant_write_reason is not UNSET:
            field_dict["cantWriteReason"] = cant_write_reason
        if last_message is not UNSET:
            field_dict["lastMessage"] = last_message

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.message import Message

        d = dict(src_dict)
        chat_id = d.pop("chatId")

        type_ = ChatType(d.pop("type"))

        title = d.pop("title")

        status = ChatStatus(d.pop("status"))

        can_write = d.pop("canWrite")

        last_event_at = d.pop("lastEventAt")

        user_id = d.pop("userId", UNSET)

        group_id = d.pop("groupId", UNSET)

        owner_id = d.pop("ownerId", UNSET)

        members_count = d.pop("membersCount", UNSET)

        _cant_write_reason = d.pop("cantWriteReason", UNSET)
        cant_write_reason: ChatCantWriteReason | Unset
        if isinstance(_cant_write_reason, Unset):
            cant_write_reason = UNSET
        else:
            cant_write_reason = ChatCantWriteReason(_cant_write_reason)

        _last_message = d.pop("lastMessage", UNSET)
        last_message: Message | Unset
        if isinstance(_last_message, Unset):
            last_message = UNSET
        else:
            last_message = Message.from_dict(_last_message)

        chat = cls(
            chat_id=chat_id,
            type_=type_,
            title=title,
            status=status,
            can_write=can_write,
            last_event_at=last_event_at,
            user_id=user_id,
            group_id=group_id,
            owner_id=owner_id,
            members_count=members_count,
            cant_write_reason=cant_write_reason,
            last_message=last_message,
        )

        chat.additional_properties = d
        return chat

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

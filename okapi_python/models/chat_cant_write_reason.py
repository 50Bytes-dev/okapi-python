from enum import Enum


class ChatCantWriteReason(str, Enum):
    INACTIVE = "inactive"
    NOT_ADMIN = "not_admin"
    NOT_MEMBER = "not_member"
    RESTRICTED = "restricted"

    def __str__(self) -> str:
        return str(self.value)

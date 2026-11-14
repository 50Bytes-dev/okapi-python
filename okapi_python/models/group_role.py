from enum import Enum


class GroupRole(str, Enum):
    MEMBER = "member"
    MODERATOR = "moderator"

    def __str__(self) -> str:
        return str(self.value)

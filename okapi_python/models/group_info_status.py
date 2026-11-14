from enum import Enum


class GroupInfoStatus(str, Enum):
    ACTIVE = "active"
    BLOCKED = "blocked"
    DELETED = "deleted"

    def __str__(self) -> str:
        return str(self.value)

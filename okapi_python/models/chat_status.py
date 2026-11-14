from enum import Enum


class ChatStatus(str, Enum):
    ACTIVE = "active"
    BLOCKED = "blocked"
    CLOSED = "closed"
    LEFT = "left"
    REMOVED = "removed"

    def __str__(self) -> str:
        return str(self.value)

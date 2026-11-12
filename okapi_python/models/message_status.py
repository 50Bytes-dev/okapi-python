from enum import Enum


class MessageStatus(str, Enum):
    EDITED = "edited"
    REMOVED = "removed"

    def __str__(self) -> str:
        return str(self.value)

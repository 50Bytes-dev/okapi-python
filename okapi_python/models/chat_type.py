from enum import Enum


class ChatType(str, Enum):
    CHANNEL = "channel"
    CHAT = "chat"
    GROUP = "group"
    SELF = "self"
    USER = "user"

    def __str__(self) -> str:
        return str(self.value)

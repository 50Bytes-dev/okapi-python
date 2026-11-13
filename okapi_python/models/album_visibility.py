from enum import Enum


class AlbumVisibility(str, Enum):
    CLASSMATES = "classmates"
    CLOSE_FRIENDS = "close_friends"
    COLLEAGUES = "colleagues"
    COURSEMATES = "coursemates"
    FELLOW_SOLDIERS = "fellow_soldiers"
    FRIENDS = "friends"
    PARTNER = "partner"
    PRIVATE = "private"
    PUBLIC = "public"
    RELATIVES = "relatives"

    def __str__(self) -> str:
        return str(self.value)

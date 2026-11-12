from enum import Enum


class MessageAttachmentType(str, Enum):
    AUDIO = "audio"
    FILE = "file"
    OTHER = "other"
    PHOTO = "photo"
    STICKER = "sticker"
    VIDEO = "video"

    def __str__(self) -> str:
        return str(self.value)

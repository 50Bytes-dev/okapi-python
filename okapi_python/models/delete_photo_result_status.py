from enum import Enum


class DeletePhotoResultStatus(str, Enum):
    DELETED = "deleted"
    FAILED = "failed"
    FORBIDDEN = "forbidden"
    NOT_FOUND = "not_found"
    SKIPPED = "skipped"

    def __str__(self) -> str:
        return str(self.value)

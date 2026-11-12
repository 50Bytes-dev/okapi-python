from enum import Enum


class LoginStep(str, Enum):
    DONE = "done"
    FAILED = "failed"
    NONE = "none"
    QR = "qr"

    def __str__(self) -> str:
        return str(self.value)

from enum import Enum


class PauseReason(str, Enum):
    CAPTCHA = "captcha"
    RESTRICTED = "restricted"
    SPAM = "spam"

    def __str__(self) -> str:
        return str(self.value)

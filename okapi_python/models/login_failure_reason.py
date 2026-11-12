from enum import Enum


class LoginFailureReason(str, Enum):
    CANCELLED = "cancelled"
    EXPIRED = "expired"
    FAILED = "failed"
    UNAVAILABLE = "unavailable"
    VERIFICATION_REQUIRED = "verification_required"

    def __str__(self) -> str:
        return str(self.value)

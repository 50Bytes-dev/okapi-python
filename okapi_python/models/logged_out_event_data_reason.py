from enum import Enum


class LoggedOutEventDataReason(str, Enum):
    BLOCKED = "blocked"
    REVOKED = "revoked"
    VERIFICATION_REQUIRED = "verification_required"

    def __str__(self) -> str:
        return str(self.value)

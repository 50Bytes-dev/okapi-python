from enum import Enum


class EventType(str, Enum):
    ALL = "All"
    CHATUPDATED = "ChatUpdated"
    CONNECTED = "Connected"
    DISCONNECTED = "Disconnected"
    LOGGEDOUT = "LoggedOut"
    LOGINUPDATED = "LoginUpdated"
    MESSAGE = "Message"
    MESSAGEEDITED = "MessageEdited"
    MESSAGESDELETED = "MessagesDeleted"
    MESSAGESREAD = "MessagesRead"
    PAUSED = "Paused"
    RESUMED = "Resumed"
    TYPING = "Typing"

    def __str__(self) -> str:
        return str(self.value)

"""Exception handling module"""
from functools import wraps


class QvevriError(Exception):
    """Base exception for Qvevri related errors"""

    def __init__(self, message):
        super().__init__(message)
        self.message = message


class GameConfigError(QvevriError):
    """Throw this error when the game configuration prevents the game from
    running properly.
    """


def watch_qvevri_errors(function):
    """Decorator used to catch QvevriError exceptions and send events"""

    @wraps(function)
    def wrapper(*args, **kwargs):
        """Catch all QvevriError exceptions and emit an event."""
        try:
            return function(*args, **kwargs)
        except QvevriError as ex:
            game = args[0]
            game.emit("game-error", ex.message)

    return wrapper

"""File-based logging for Dramora's Idle Upgrade Tree."""

from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path

LOG_FOLDER = Path("logs")
LOG_FILE = LOG_FOLDER / "latest.log"


class Logging:
    """Append timestamped messages to logs/latest.log."""

    def init(self) -> None:
        """Initialize the logging system."""
        LOG_FOLDER.mkdir(parents=True, exist_ok=True)
        if not LOG_FILE.exists():
            LOG_FILE.write_text("", encoding="utf-8")

    def _write(self, message: str, level: str) -> None:
        """Write a message to the log file."""
        self.init()
        stamp = datetime.now(timezone.utc).isoformat()
        with LOG_FILE.open("a", encoding="utf-8") as handle:
            handle.write(f"[{stamp}] [{level}] {message}\n")

    def info(self, message: str) -> None:
        """Write an info message to the log file."""
        self._write(message, "INFO")

    def error(self, message: str) -> None:
        """Write an error message to the log file."""
        self._write(message, "ERROR")

    def warn(self, message: str) -> None:
        """Write a warning message to the log file."""
        self._write(message, "WARN")

    def debug(self, message: str) -> None:
        """Write a debug message to the log file."""
        self._write(message, "DEBUG")

    def trace(self, message: str) -> None:
        """Write a trace message to the log file."""
        self._write(message, "TRACE")

    def fatal(self, message: str) -> None:
        """Write a fatal message to the log file."""
        self._write(message, "FATAL")


logging = Logging()

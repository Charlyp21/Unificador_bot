from dataclasses import dataclass
from pathlib import Path
import os


@dataclass(frozen=True)
class Settings:
    telegram_token: str
    contacts_file: Path
    community_file: Path
    google_calendar_api_key: str = ""
    google_calendar_id: str = ""
    log_level: str = "INFO"

    @classmethod
    def from_env(cls, base_dir: Path) -> "Settings":
        token = os.getenv("TELEGRAM_TOKEN", "").strip()
        if not token:
            raise ValueError("Missing TELEGRAM_TOKEN in environment variables.")
        contacts_path = os.getenv("CONTACTS_FILE", "data/contactos.json")
        community_path = os.getenv("COMMUNITY_FILE", "data/comunidad.json")
        google_calendar_api_key = os.getenv("GOOGLE_CALENDAR_API_KEY", "").strip()
        google_calendar_id = os.getenv("GOOGLE_CALENDAR_ID", "").strip()
        log_level = os.getenv("LOG_LEVEL", "INFO").upper()

        return cls(
            telegram_token=token,
            contacts_file=base_dir / contacts_path,
            community_file=base_dir / community_path,
            google_calendar_api_key=google_calendar_api_key,
            google_calendar_id=google_calendar_id,
            log_level=log_level,
        )

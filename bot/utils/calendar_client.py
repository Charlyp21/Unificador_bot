from datetime import datetime, timezone
from typing import Any

from googleapiclient.discovery import build


def get_next_events(
    api_key: str,
    calendar_id: str,
    max_results: int = 5,
) -> list[dict[str, Any]]:
    service = build("calendar", "v3", developerKey=api_key, cache_discovery=False)
    now_utc = datetime.now(timezone.utc).isoformat()

    response = (
        service.events()
        .list(
            calendarId=calendar_id,
            timeMin=now_utc,
            maxResults=max_results,
            singleEvents=True,
            orderBy="startTime",
        )
        .execute()
    )

    return response.get("items", [])

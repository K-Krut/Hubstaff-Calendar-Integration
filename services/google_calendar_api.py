from datetime import datetime, timedelta
from services.google_auth import get_calendar_service

from core.config import settings


def convert_activity_to_event(activity: dict):
    starts_at = datetime.fromisoformat(activity["starts_at"].replace("Z", "+00:00"))
    ends_at = starts_at + timedelta(seconds=activity.get("tracked", 0))

    return {
        "summary": "Work SCS / tracking",
        "start": {
            "dateTime": starts_at.isoformat(),
            "timeZone": "UTC",
        },
        "end": {
            "dateTime": ends_at.isoformat(),
            "timeZone": "UTC",
        },
    }


def create_event_in_calendar(calendar, calendar_id, event):
    return calendar.events().insert(calendarId=calendar_id, body=event).execute()


def add_activities_to_calendar(activities, calendar_id=settings.CALENDAR_ID):
    response = []
    for activity in activities:
        calendar = get_calendar_service()
        event = convert_activity_to_event(activity)
        response.append(create_event_in_calendar(calendar, calendar_id, event))

    return response

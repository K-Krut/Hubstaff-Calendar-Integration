from datetime import datetime, timedelta
from services.google_auth import get_calendar_service

from core.config import settings


def convert_activity_to_event(activity: dict):
    return {
        "summary": "Work SCS / tracking",
        "start": {
            "dateTime": activity["start"],
            "timeZone": settings.TIMEZONE,
        },
        "end": {
            "dateTime": activity["end"],
            "timeZone": settings.TIMEZONE,
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

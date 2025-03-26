import logging
from http.client import HTTPException
from fastapi import APIRouter, HTTPException, status

from schemas.calendar import HubstaffSyncRequest
from services.google_calendar_api import add_activities_to_calendar
from services.hubstaff_api import get_activities
from services.hubstaff_auth import get_access_token
from utils.activities import merge_activities

router = APIRouter()
logger = logging.getLogger(__name__)


@router.post("/hubstaff/sync")
def sync_hubstaff_to_calendar(data: HubstaffSyncRequest):
    try:
        access_token = get_access_token()
        activities_response = get_activities(access_token, data.date_start, data.date_end)
        activities = merge_activities(activities_response.get('activities', []))
        response = add_activities_to_calendar(activities)
        return {"events_number": len(response), "events": response}
    except HTTPException as error:
        raise error
    except Exception as error:
        logger.error(f'----#ERROR in POST /api/calendar/hubstaff/sync: {error}')
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Internal server error\n{error}")


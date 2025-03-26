import logging
from http.client import HTTPException
from fastapi import APIRouter, Depends, HTTPException, status, Response, Query


router = APIRouter()
logger = logging.getLogger(__name__)


@router.post("/hubstaff/sync")
def sync_hubstaff_to_calendar():
    try:
        return {}
    except HTTPException as error:
        raise error
    except Exception as error:
        logger.error(f'----#ERROR in POST /api/calendar/hubstaff/sync: {error}')
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Internal server error\n{error}")


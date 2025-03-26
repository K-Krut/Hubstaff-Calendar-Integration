from pydantic import BaseModel


class HubstaffSyncRequest(BaseModel):
    date_start: str
    date_end: str
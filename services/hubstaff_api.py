import requests

from core.config import settings


def get_activities(token, start, end):
    res = requests.get(
        f"{settings.HUBSTAFF_API_URL}/v2/organizations/{settings.HUBSTAFF_ORG_ID}/activities/daily?"
        f"page_limit=500&date[start]={start}&date[stop]={end}user_ids[]={settings.HUBSTAFF_USER_ID}",
        headers={
            "Authorization": f"Bearer {token}"
        }
    )

    if res.status_code != 200:
        raise Exception(f"Hubstaff error: {res.status_code} - {res.text}")

    return res.json()



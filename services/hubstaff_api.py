import requests

from core.config import settings


def get_activities(token, start, end):
    res = requests.get(
        f"https://api.hubstaff.com/v2/organizations/{settings.HUBSTAFF_ORG_ID}/activities",
        headers={"Authorization": f"Bearer {token}"},
        params={
            "time_slot[start]": start,
            "time_slot[stop]": end,
            "user_ids[]": settings.HUBSTAFF_USER_ID,
            "page_limit": 500
        }
    )

    if res.status_code != 200:
        raise Exception(f"{res.status_code}\n{res.text}")

    return res.json()

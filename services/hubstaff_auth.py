import json
import os

import requests

from core.config import settings


def refresh_access_token():
    response = requests.post(
        f"https://account.hubstaff.com/access_tokens?grant_type=refresh_token&refresh_token=",
    )

    if response.status_code != 200:
        raise Exception(f"{response.status_code} - {response.text}")

    return response.json()


def load_hubstaff_tokens():
    if not os.path.exists(settings.HUBSTAFF_TOKENS):
        return None
    with open(settings.HUBSTAFF_TOKENS_PATH) as f:
        return json.load(f)


def get_access_token():
    pass

print(load_hubstaff_tokens())
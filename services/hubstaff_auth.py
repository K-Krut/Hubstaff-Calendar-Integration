import datetime
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
    with open(settings.HUBSTAFF_TOKENS_PATH) as f:
        return json.load(f)


def save_hubstaff_tokens(tokens):
    tokens["expire_at"] = datetime.datetime.now() + datetime.timedelta(seconds=tokens.get('expires_in'))
    with open(settings.HUBSTAFF_TOKENS_PATH, "w+") as file:
        json.dump(tokens, file)


def is_token_expired(tokens_data):
    return datetime.datetime.fromisoformat(tokens_data.get("expire_at")) < datetime.datetime.now()


def get_access_token():
    data = load_hubstaff_tokens()


data = load_hubstaff_tokens()
print(data)
print(is_token_expired(data))
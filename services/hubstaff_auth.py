import requests


def refresh_access_token():
    response = requests.post(
        f"https://account.hubstaff.com/access_tokens?grant_type=refresh_token&refresh_token={}",
    )

    if response.status_code != 200:
        raise Exception(f"{response.status_code} - {response.text}")

    return response.json()



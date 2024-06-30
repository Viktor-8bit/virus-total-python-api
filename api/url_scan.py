


import json
import requests
from .api_key import api_key


# scan url
def url_scan(scan_url: str) -> str:

    virustotal_url = "https://www.virustotal.com/api/v3/urls"

    payload = { "url": scan_url }

    headers = {
        "accept": "application/json",
        "x-apikey": api_key,
        "content-type": "application/x-www-form-urlencoded"
    }

    response_text = requests.post(virustotal_url, data=payload, headers=headers).text

    json_data = json.loads(response_text)
    return json_data['data']['links']['self']


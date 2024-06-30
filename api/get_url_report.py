


import json
import requests
from .api_key import api_key
from .report import report

# get url report
def get_url_report(scaned_url: str) -> report: 


    headers = {
        "accept": "application/json",
        "x-apikey": api_key
    }

    response_text = requests.get(scaned_url, headers=headers).text
    json_data = json.loads(response_text)
    url_report = report(responce=json_data)
    
    return url_report
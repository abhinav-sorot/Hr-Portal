import time
from datetime import datetime
import json

import pytest
import requests

def test_morning():

    try:
        latest_date = datetime.today().strftime('%Y-%m-%d')
        url = "https://hroneauthapi.hrone.cloud/oauth2/token"

        payload = 'username=abhinav.sorot%2540qentelli.com&password=%2523Abh1nav&grant_type=password&loginType=1&companyDomainCode=qentelli'
        headers = {
            'authority': 'hroneauthapi.hrone.cloud',
            'Authorization': 'Bearer',
            'Origin': 'https://app.hrone.cloud',
            'Referer': 'https://app.hrone.cloud/',
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        response = requests.request("POST", url, headers=headers, data=payload)
        assert response.status_code ==200
        json_resp = json.loads(response.text)
        access_token = json_resp['access_token']

        url = "https://hronewebapi.hrone.cloud/api/timeoffice/mobile/checkin/Attendance/Request"
        headers = {
            'authority': 'hronewebapi.hrone.cloud',
            'domaincode': 'qentelli',
            'Origin': 'https://app.hrone.cloud',
            'Referer': 'https://app.hrone.cloud/',
            'Authorization': f'Bearer {access_token}',

            'Content-Type': 'application/json'
        }

        payload = "{\n    \"requestType\": \"A\",\n    \"employeeId\": 116,\n    \"latitude\": " \
                  "\"\",\n    \"longitude\": \"\",\n    \"geoAccuracy\": \"\"," \
                  f"\n    \"geoLocation\": \"\",\n    \"punchTime\": \"{latest_date}T10:25\"," \
                  "\n    \"uploadedPhotoOneName\": \"\",\n    \"uploadedPhotoOnePath\": \"\",\n    \"uploadedPhotoTwoName\": \"\",\n    \"uploadedPhotoTwoPath\": \"\",\n    \"attendanceSource\": \"W\",\n    \"attendanceType\": \"Online\"\n}"

        response = requests.request("POST", url, headers=headers, data=payload)
        assert response.status_code ==200
        print(f"Attendance marked at {time} for {latest_date}")
        
    except Exception as e:
        assert False

def test_evening():

    try:
        latest_date = datetime.today().strftime('%Y-%m-%d')
        url = "https://hroneauthapi.hrone.cloud/oauth2/token"

        payload = 'username=abhinav.sorot%2540qentelli.com&password=%2523Abh1nav&grant_type=password&loginType=1&companyDomainCode=qentelli'
        headers = {
            'authority': 'hroneauthapi.hrone.cloud',
            'Authorization': 'Bearer',
            'Origin': 'https://app.hrone.cloud',
            'Referer': 'https://app.hrone.cloud/',
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        response = requests.request("POST", url, headers=headers, data=payload)
        assert response.status_code ==200
        json_resp = json.loads(response.text)
        access_token = json_resp['access_token']

        url = "https://hronewebapi.hrone.cloud/api/timeoffice/mobile/checkin/Attendance/Request"
        headers = {
            'authority': 'hronewebapi.hrone.cloud',
            'domaincode': 'qentelli',
            'Origin': 'https://app.hrone.cloud',
            'Referer': 'https://app.hrone.cloud/',
            'Authorization': f'Bearer {access_token}',

            'Content-Type': 'application/json'
        }

        payload = "{\n    \"requestType\": \"A\",\n    \"employeeId\": 116,\n    \"latitude\": " \
                  "\"\",\n    \"longitude\": \"\",\n    \"geoAccuracy\": \"\"," \
                  f"\n    \"geoLocation\": \"\",\n    \"punchTime\": \"{latest_date}T20:00\"," \
                  "\n    \"uploadedPhotoOneName\": \"\",\n    \"uploadedPhotoOnePath\": \"\",\n    \"uploadedPhotoTwoName\": \"\",\n    \"uploadedPhotoTwoPath\": \"\",\n    \"attendanceSource\": \"W\",\n    \"attendanceType\": \"Online\"\n}"

        response = requests.request("POST", url, headers=headers, data=payload)
        assert response.status_code ==200
        print(f"Attendance marked at {time} for {latest_date}")
        
    except Exception as e:
        assert False

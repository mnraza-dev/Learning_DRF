import requests
import json

URL = 'http://127.0.0.1:8000/create/'

data = {
    'name': 'Soni',
    'roll': 106,
    'city': 'Hyderabad'
}

json_data = json.dumps(data)
headers = {'Content-Type': 'application/json'}
r = requests.post(url=URL, data=json_data, headers=headers)

if r.status_code == 200:
    try:
        # Try to parse the JSON response
        data = r.json()
        print(data)
    except ValueError as e:
        print("Error decoding JSON:", e)
        print("Raw response:", r.text)
else:
    print("Request failed with status code:", r.status_code)

import requests
import json

URL = "http://127.0.0.1:8000/studentapi/"

def get_data(id=None):
    params = {}
    if id is not None:
        params = {'id': id}
    
    r = requests.get(url=URL, params=params)
    
    if r.status_code == 200:
        data = r.json()  
        print(data)
    else:
        print(f"Failed to get data. Status code: {r.status_code}")


get_data() 
# get_data(1) 
import requests
import sys
import json

from record import record

def request_api(username: str):
    page = 1
    while True:
         url = "https://api.github.com/users/"+username+"/followers?page="+str(page)+"&per_page=100"
         req = requests.get(url)
         if req.status_code == 200:
            data = req.json() 
            if len(data) == 0:
                break
            else:
                record(data)
                page = page + 1
         else:
            print("request status_code:"+str(req.status_code))
            sys.exit(-1)
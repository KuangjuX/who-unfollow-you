import requests
import sys

def request_api(username: str) -> list:
    page = 1
    followers = []
    while True:
         url = "https://api.github.com/users/"+username+"/followers?page="+str(page)+"&per_page=100"
         req = requests.get(url)
         if req.status_code == 200:
            data = req.json() 
            if len(data) == 0:
                break
            else:
                followers += data
                page += 1
         else:
            print("URL: " + url)
            print("request status_code:"+str(req.status_code))
            sys.exit(-1)
    return followers
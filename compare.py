import datetime
import json

def compare():
    today = datetime.date.today()
    yesterday = today - datetime.timedelta(days = 1)

    today_file = "./followers/"+str(today)+".json"
    yesterday_file = "./followers/"+str(yesterday)+".json"

    f1 = open(today_file, 'r')
    today_json = json.loads(f1.read())
    f1.close()

    f2 = open(yesterday_file, 'r')
    yesterday_json = json.loads(f2.read())
    f2.close()

    today_followers = map(lambda info: info.login, today_json)
    yesterday_followers = map(lambda info: info.login, yesterday_json)

    for _, follower in yesterday_followers.enumerate():
        if follower in today_followers == False:
            print("username: " + follower)

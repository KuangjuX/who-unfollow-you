from request import request_api
from file import read_followers, record
from log import log

def fetch_user(info):
    return info['login']

def unfollow(username):
    followers = request_api(username)
    records = read_followers()

    followers_username = list(map(fetch_user, followers))
    records_username = list(map(fetch_user, records))

    for _, user in enumerate(records_username):
        if user not in followers_username:
            log(user)

    record(followers)


import datetime
def log(user):
    with open('./log.txt', 'a+') as f:
        today = datetime.date.today()
        msg = "User " + user + 'unfollowed you.'
        msg += "    ------ " + str(today) + '\n'
        f.write(msg)
import datetime


def log(user):
    today = datetime.date.today()
    msg = "User " + user + " unfollowed you."
    msg += "    ------ " + str(today) + '\n'

    with open('./log.txt', 'a+') as f:
        f.write(msg)

    print(msg)

def log(user):
    with open('./log.txt', 'a+') as f:
        msg = "User " + user + 'unfollowed you.\n'
        print(msg)
        f.write(msg)
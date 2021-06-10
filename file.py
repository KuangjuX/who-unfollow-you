import json

def record(data):
    file = './followers.json'
    with open (file, mode='w', encoding = 'gbk') as f:
        json_data = json.dumps(data)
        f.write(json_data)


def read_followers() -> list:
    file = './followers.json'
    f = open(file, 'r')
    data = f.read()
    f.close()
    return json.loads(data)
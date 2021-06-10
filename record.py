import datetime
import json

def record(data):
    date = str(datetime.date.today())
    file = './followers/' + date + '.json'
    with open (file, mode='w', encoding = 'gbk') as f:
        json_data = json.dumps(data)
        f.write(json_data)
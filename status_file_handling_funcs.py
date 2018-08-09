import json

def save_statuses(statuses):
    file_path="/tmp/blinkt_device_statuses"
    json_string=json.dumps(statuses)
    json_file=open(file_path,"w")
    json_file.write(json_string)

def load_statuses():
    file_path="/tmp/blinkt_device_statuses"
    try:
        json_file=open(file_path,"r")
        json_string=json_file.read()
        statuses=json.loads(json_string)
    except IOError:
        json_file=open(file_path,"w")
        json_file.close()
        json_string=""
        statuses={}
    return statuses

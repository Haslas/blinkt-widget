import requests
import avahi
import status_file_handling_funcs as sfhf
from time import sleep

def get_device_list():
    '''Returns a list of ips of devices'''
    device_list = []
    blinkt_devices = avahi.read()
    # print(blinkt_devices)
    for item in blinkt_devices:
        device_list.append(item)
    # print(device_list)
    return device_list


def get_device_statuses():
    errorTuple = (
        SyntaxError,
        AttributeError,
        TypeError,
        requests.exceptions.Timeout,
        requests.exceptions.ConnectTimeout,
        requests.exceptions.ConnectionError,
        RuntimeError)
    statuses = []
    device_list = get_device_list()
    for device in device_list:
        # This line would make http://localhost:5000
        # into http://localhost:5000/api
        device = device.strip()
        print('http://' + device + '/api')
        try:
            response = requests.get('http://' + device + '/api', timeout=1)
            print(response)
            # builds a dict list of statuses and the type of device
            statuses.append(response.json())
        except errorTuple:
            statuses.append({'missing': device})
    return statuses

def run():
     # Counter is used to pad out avahi.browse():
    counter=0
    while True:
        statuses=get_device_statuses()
        sfhf.save_statuses(statuses)
        sleep(10)
        if counter==12:
            avahi.write(avahi.browse())
            counter=0
        counter+=1


if __name__ == "__main__":
    avahi.run()
    run()

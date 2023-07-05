import json
import sys
import requests


def CloudPrint():
    r = requests.post("http://云平台地址/Users/Login", data={"Account": "【username】", "Password": "【password】]", "IsRememberMe": "true"})
    token = json.loads(r.text)["ResultObj"]["AccessToken"]
    r = requests.get("http://云平台地址/devices/设备ID/sensors/设备标识", headers={"AccessToken": token})
    temp = json.loads(r.text)["ResultObj"]['Value']
    r = requests.get("http://云平台地址/devices/设备ID/sensors/设备标识", headers={"AccessToken": token})
    humi = json.loads(r.text)["ResultObj"]['Value']
    print("温度:",temp)
    print("湿度:",humi)

if __name__ == '__main__':
    CloudPrint()

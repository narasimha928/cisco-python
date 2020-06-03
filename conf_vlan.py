#!/usr/bin/env python
# create a vlan using RestAPI
import requests
import json
requests.packages.urllib3.disable_warnings()

ip = '172.29.207.8'
vlanId = '1401'

myheaders = {'content-type': 'application/json-rpc'}
url = "https://"+ip+"/ins"
username = "admin"
password = "insieme"


payload = [
    {"jsonrpc": "2.0", "method": "cli", "params": {"cmd": "vlan "+vlanId, "version": 1}, "id": 2},
]

response = requests.post(url, data=json.dumps(payload), headers=myheaders,
                         auth=(username, password), verify=False).json()
print("Responce:", response)

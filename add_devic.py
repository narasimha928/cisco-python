#!/usr/bin/env python
import requests
from auth_token import get_token
from pprint import pprint
requests.packages.urllib3.disable_warnings()

def main():

  new_device_dict = {
		"ipAddress": ["192.0.2.1"],
		"snmpVersion": "v2",
		"snmpROCommunity": "readonly",
		"snmpRWCommunity": "readwrite",
		"snmpRetry": "1",
		"snmpTimeout": "60",
		"cliTransport": "ssh",
		"userName": "nick",
		"password": "secret123!",
		"enablePassword": "secret456!",
		}

  token = get_token()

  api_path = "https://sandboxdnac.cisco.com/dna"
  headers = {"Content-Type":"application/json","X-Auth-Token":token}

  add_res = requests.post(f"{api_path}/intent/api/v1/network-device",json=new_device_dict,headers=headers,)
  print(add_res.json())

if __name__ == '__main__':

  main()

  

#!/usr/bin/env python
import requests
from auth_token import get_token
from pprint import pprint

def main():


  token = get_token()

  api_path = "https://sandboxdnac.cisco.com/dna"
  headers = {"Content-Type":"application/json","X-Auth-Token":token}

  get_resp = requests.get(f"{api_path}/intent/api/v1/network-device",headers = headers)

  if get_resp.ok:
    for device in get_resp.json()['response']:
      print(f" ID : {device['id']}, IP:i{device['managementIpAddress']}")
  else:
    print(f"failure body: {get_resp.text}")


if __name__ == '__main__':

  main()

  

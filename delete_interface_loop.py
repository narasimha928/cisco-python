#!/usr/bin/env python3
import requests
requests.packages.urllib3.disable_warnings()

USER = 'developer'
PASS = 'C1sco12345'


headers = {'Content-Type':'application/yang-data+json',
           'Accept':'application/yang-data+json'
          }

int_number = 5
for x in range(int_number):
  
  intname = "Loopback123" + str(x)
  print('Deleting Loopback : ',intname)
  payload = {}
  url = "https://ios-xe-mgmt.cisco.com:9443/restconf/data/ietf-interfaces:interfaces/interface=" + intname
  response=requests.request('DELETE',url, auth=(USER, PASS), headers=headers, data=payload,  verify=False)
  print('Status Code:',	response.status_code)
  print('Response Text:',response.text)




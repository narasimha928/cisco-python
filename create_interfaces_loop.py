#!/usr/bin/env python3
import requests
requests.packages.urllib3.disable_warnings()

USER = 'developer'
PASS = 'C1sco12345'


url = "https://ios-xe-mgmt.cisco.com:9443/restconf/data/ietf-interfaces:interfaces"
headers = {'Content-Type':'application/yang-data+json',
           'Accept':'application/yang-data+json'
          }

int_number = 5
for x in range(int_number):
  ipaddr = '1.2.3.{}'.format(x)
  print('Creating Loopback : ',ipaddr)

  payload = '\
        {\
        "interface": {\
        "name": "Loopback123' + str(x) + '",\
        "description": "CONFIGURED WITH POSTMAN - ABADEE - CCNP ENCOR",\
        "type": "iana-if-type:softwareLoopback",\
        "enabled": true,\
        "ietf-ip:ipv4": {\
          "address": [	\
            {\
              "ip": "1.2.3.' + str(x) + '",\
              "netmask": "255.255.255.255"\
            }\
          ]\
        }\
        }\
     }\
    '


  response=requests.request('POST',url, auth=(USER, PASS), headers=headers, data=payload,  verify=False)
  print('Status Code:',	response.status_code)
  print('Response Text:',response.text)




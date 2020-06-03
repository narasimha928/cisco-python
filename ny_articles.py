#!/usr/bin/env python


import requests
from bs4 import BeautifulSoup
 
base_url = 'http://www.nytimes.com'
r = requests.get(base_url)
soup = BeautifulSoup(r.text,'lxml')
print(soup.prettify()) 

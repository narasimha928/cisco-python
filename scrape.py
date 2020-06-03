#!/usr/bin/env python

from bs4 import BeautifulSoup

with open('simple.html') as html_file:
  soup = BeautifulSoup(html_file,'lxml')

print(soup.find('div',class_="footer"))

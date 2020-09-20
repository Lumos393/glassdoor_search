import sys
import os
import requests
from bs4 import BeautifulSoup
import lxml

reqs = requests.get(
    'http://api.glassdoor.com/api/api.htm?v=1&format=json&t.p=120&t.k=fz6JLNDfgVs&action=employers&q=pharmaceuticals&userip=192.168.43.42&useragent=Mozilla/%2F4.0')
soup = BeautifulSoup(reqs.text, 'lxml')

print(reqs)

import sys
import os
import requests
from bs4 import BeautifulSoup
import lxml
from urllib.request import urlopen, Request
from requests.api import request

user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'

#url = 'https://www.glassdoor.com/Job/suwanee-human-resources-jobs-SRCH_IL.0,7_IC1155695_KE8,23.htm?'
url = 'https://www.wikipedia.org/'

headers = {'User-Agent':user_agent,}
request = Request(url, None, headers)
page = urlopen(url)

data = page.read()
print(data)

html_bytes = page.read()
html = html_bytes.decode('utf-8')

print(html)

reqs = requests.get(url)
soup = BeautifulSoup(reqs.text, 'lxml')

print(soup.find_all('span'))

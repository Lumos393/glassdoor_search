import sys
import os
import requests
from bs4 import BeautifulSoup
import lxml

url = 'https://www.glassdoor.com/Job/suwanee-human-resources-jobs-SRCH_IL.0,7_IC1155695_KE8,23.htm?'

reqs = requests.get(url)
soup = BeautifulSoup(reqs.text, 'lxml')

print(soup.find_all('span'))
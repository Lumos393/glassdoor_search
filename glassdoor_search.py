from re import findall
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
from bs4 import element
from requests.api import request

user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'

url = 'https://www.glassdoor.com/Job/suwanee-human-resources-jobs-SRCH_IL.0,7_IC1155695_KE8,23.htm?'
headers = {'User-Agent':user_agent}
req = Request(url, None, headers)

page = urlopen(req)

html_bytes = page.read()
soup = BeautifulSoup(html_bytes, 'html.parser')
#strhtm = soup.prettify()
mysoup = soup.findAll('li', {'class': 'jl react-job-listing gdGrid'})

mysoupy = soup.attrs.fromkeys(mysoup)

for x in mysoup:
    print(x, '\n')

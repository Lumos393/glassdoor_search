from re import error, findall
from bs4 import BeautifulSoup, element
from urllib.request import urlopen, Request

user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'

url = 'https://www.glassdoor.com/Job/suwanee-human-resources-jobs-SRCH_IL.0,7_IC1155695_KE8,23.htm?'
headers = {'User-Agent':user_agent}
req = Request(url, None, headers)

page = urlopen(req)

html_bytes = page.read()
soup = BeautifulSoup(html_bytes, 'html.parser')
#strhtm = soup.prettify()

soupy_mess = []

for li in soup.findAll('li', {'class': 'jl react-job-listing gdGrid'}):
    soupy_mess.append(li['data-normalize-job-title'])
    soupy_mess.append(soup.find('span'))

print(soupy_mess)
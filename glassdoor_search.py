import sys
import os
import requests
from bs4 import BeautifulSoup
import lxml

#https: // www.glassdoor.com/Job/jobs.htm?suggestCount = 0 & suggestChosen = false & clickSource = searchBtn & typedKeyword = human+resources & locT = C & locId = 1155695 & jobType = &context = Jobs & sc.keyword = human+resources & dropdown = 0

url = "https://www.glassdoor.com/Job/jobs.htm?suggestCount=0&suggestChosen=false&clickSource=searchBtn&typedKeyword=human+resources&locT=C&locId=1155695&jobType=&context=Jobs&sc.keyword=human+resources&dropdown=0"

reqs = requests.get(url)

soup = BeautifulSoup(reqs.text, "lxml")

print(soup.find_all("span"))
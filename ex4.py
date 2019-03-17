from requests import get
from bs4 import BeautifulSoup

#target site
url = "https://www.goal.com/en-in/team/real-madrid/fixtures-results/3kq9cckrnlogidldtdie2fkbl"

#get data from site
response = get(url)

#print data
print(response.status_code)

#get raw html data
match = BeautifulSoup(response.content, "html.parser")

#view the html data
#print(match.prettify)
#match_div = match.findAll('div')
#match_div = match.findAll('div', {"class":"match-data"})
#match_div = match.findAll('div', {"class":"team-away win"})
#match_div = match.find({"class":"team-name"})
#match_div = match.findAll('div', {"class":"team-away win"})
#opponent = match.find('span', {"class":"team-name"})
#opponent = match.find('span', {"class":"team-away win"})
opponent = match.findAll('span', {"class":"team-name"})

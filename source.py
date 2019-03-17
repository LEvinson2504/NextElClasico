import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

#target url
my_url = 'https://www.goal.com/en-in/team/real-madrid/fixtures-results/3kq9cckrnlogidldtdie2fkbl'

#grap webpage, opening connection
uClient = uReq(my_url)

#raw html
page_html = uClient.read()

#close connection
uClient.close()

#html parsing
page_soup = soup(page_html, "html.parser")

#graps the matches
containers = page_soup.findAll("div", {"class":"match-data"})

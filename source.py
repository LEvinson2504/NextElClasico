'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

from requests import get
from bs4 import BeautifulSoup
from lxml import html
import datetime
from datetime import datetime
from pytz import timezone

#target site
url = "https://www.goal.com/en-in/team/real-madrid/fixtures-results/3kq9cckrnlogidldtdie2fkbl"

#get data from site
response = get(url)

#print status code
#print(response.status_code)

#get raw html data
tree = html.fromstring(response.content)

#get the dates
dates = tree.xpath("//a[@class='match-main-data-link']/div/span[not(text())]/../time")
dates = [date.get('datetime') for date in dates]

#get the teams
teams = tree.xpath("//a[@class='match-main-data-link']/div/span[not(text())]/../../div/div/div/span[@class='team-name']")
teams = [team.text for team in teams]

#print(dates)
#print(teams)

a = dict(zip(dates, teams))
#print(a)

#using valencia as no el clasico fixtures this season
team = "Valencia"
i = 0
for n in a.values():
    if (n==team):
        print(n)
        i+= 1
        t  = dates[i]
        conv_date = t[:10]
        conv_time = t[12:19]
        #print(conv_date)
        #print(conv_time)
        t2 = conv_date + " " + conv_time
        print(t2)
        
        
'''
        datetime_obj = datetime.strptime(t2, "%Y-%m-%d %H:%M:%S")
        datetime_obj_ist = datetime_obj.replace(tzinfo=timezone('UTC'))
        print (datetime_obj_ist.strftime("%Y-%m-%d %H:%M:%S %Z%z"))
'''




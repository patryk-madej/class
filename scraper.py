import lxml
import requests
from bs4 import BeautifulSoup
import fnmatch

result = requests.get('https://codebar.io/events')
src = result.content
soup = BeautifulSoup(src, 'lxml')

event_divs = soup.find_all("div",{'class': 'event'}) #create list with the html objects

events = []
for event in event_divs:
    events.append(event.getText()) #turn each complex item into text

feed = []
for e in events:
    feed.append(" ".join(e.split())) #delete all whitespaces and place single space between words

london = []
for l in feed:
    if fnmatch.fnmatch(l, '*London*'): #match only events that have 'London' in them
        london.append(l)

print(london)

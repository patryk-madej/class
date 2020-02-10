#import boto3
#import json


import lxml
import requests
from bs4 import BeautifulSoup
import fnmatch

result = requests.get('https://codebar.io/events')
src = result.content
soup = BeautifulSoup(src, 'lxml')

event_divs = soup.find_all("div",{'class': 'event'})


events = []
for event in event_divs:
    #city_span = event.find('span',{'class': 'label status'})
    #if fnmatch.filter(event, '*London*'):
    #print(fnmatch.filter(event, '*London*'))
    events.append(event.getText()) # <======= maybe turn each complex item in the list into text and then fnmatch

#print(events[3].strip()) # <====== need to delete most whitespace for readability. maybe turn \n's into spaces

feed = []
for e in events:
    feed.append(" ".join(e.split())) #deletes all whitespaces and places single space between words

london = []
for l in feed:
    if not fnmatch.filter(l, '*London*'):
        feed.remove(l)
        #london.append(l)
    elif fnmatch.filter(l, '*London*'):
        london.append(l)
    else:
        continue

print(london)

#print(event_divs[5].getText())



'''
ul_column = soup.find_all("ul")[3] #upcoming events
cities = ul_column.find_all("span")
events = []
div_tag = ul_column.find_all("div")
for x in cities:
    if re.search("London", x): 
        print(x)
    else:
        continue
for x in div_tag:
    if div_tag[x]["class"]:
        events.append(div_tag)
    else:
        continue
print(events)
'''

'''
for city in div_column:
    if city == '*London*':
        print(city)
        break
        
for div_tag in soup.find_all("div"):
    span_tag = div_tag.find("span")
    events.append(span_tag)
    print(events)
'''

#div_tag = soup.find_all("div")[9]
#coulumn that has ['class'] and also id and contains all the events in further divs

#print(div_tag)

#div_tag = soup.find_all("div")[7]
#print(div_tag.getText())

'''
for div_tag in soup.find_all("div"):
    if events.index('London'):
        print(div_tag)
    pass
'''


'''
events = soup.find_all("div")
for event in events:
    if "event" in event.text:
        print(event)
        #print(link.attrs['label status'])
'''

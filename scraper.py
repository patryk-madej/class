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

for event in event_divs:
    #city_span = event.find('span',{'class': 'label status'})
    #if fnmatch.filter(event, '*London*'):
    print(fnmatch.filter(event, '*London*'))


#print(events_divs[5].getText())



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

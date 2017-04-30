#import our libraries
import urllib, json
import scraperwiki

#a JSON file
url = "https://data.police.uk/api/forces"

#fetch the json from the URL
response = urllib.urlopen(url)
#load it into variable called x
data = json.loads(response.read())
#let's see what we have
print data
print len(data)

#create empty dictionary variable to hold our data
record = {}
#loop through each item in the data variable
for i in data:
    print i
    print i['name']
    if i['id'] == 'wiltshire':
        print 'THIS IS WILTSHIRE2'
    if 'wilt' in i['id']:
        print 'IT CONTAINS WILT'
    record['idcode'] = i['id']
    record['fullname'] = i['name']
    scraperwiki.sqlite.save(['idcode'], record)

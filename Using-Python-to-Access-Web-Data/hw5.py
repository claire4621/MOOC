#read the JSON data from a URL 
#parse and extract the comment counts from the XML data
#compute the sum of the numbers in the file
#JSON structure: {'comments':[{'name': 'Tina', 'count': 38},{'name': 'Ryan', 'count': 22},...]}
#View data: http://python-data.dr-chuck.net/comments_42.json

import urllib
import json

while True:
    address = raw_input('Enter location: ') #prompt for a URL
    if len(address) < 1 : break

    print 'Retrieving', address 
    uh = urllib.urlopen(address)
    data = uh.read()
    print data
    dictionary = json.loads(data) #return a dictionary
    print 'User count:', len(dictionary['comments'])
    sum = 0
    for user in dictionary['comments']:
        sum = sum + user['count']
    print 'Sum:', sum

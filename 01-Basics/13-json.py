#SIMPLE EXAMPLE FOR RETRIEVING JSON FILES FROM WEB

import codecs
import json
import urllib.request

url = "https://api.github.com/users/michaelcw02/repos"
req = urllib.request.Request(url)
response = urllib.request.urlopen(req)
reader = codecs.getreader("utf-8")
data = json.load(reader(response))

print(data)


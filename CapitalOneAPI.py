import requests
import json

import urllib.request
raw = urllib.request.urlopen('http://api.reimaginebanking.com/enterprise/customers?key=3bb6dcc2cfc7ec704cfd2678b2816209')
json_object = json.load(raw)

for important_data in json_object['results'][0]['address']:
    print(important_data)
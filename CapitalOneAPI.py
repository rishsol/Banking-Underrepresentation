import requests
import json
list = []
import urllib.request
#raw = urllib.request.urlopen('http://api.reimaginebanking.com/enterprise/customers?key=3bb6dcc2cfc7ec704cfd2678b2816209')
#json_object = json.load(raw)

url = 'http://api.reimaginebanking.com/enterprise/customers?key=3bb6dcc2cfc7ec704cfd2678b2816209'

json_data = requests.get(url).json()

#print(json_data)
#for address_data in json_data['results'][0]['address']:
#	print(address_data)

for i in range(len(json_data['results']) - 1):
    list.append(json_data['results'][i]['address'])

for i in range(len(list)):
    list[i] = list[i]

#print(json_data['results'][5]['address'])
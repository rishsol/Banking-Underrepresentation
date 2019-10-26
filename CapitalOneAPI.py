import requests
import json

addressList = []
addressStringList = []

url = 'http://api.reimaginebanking.com/enterprise/customers?key=3bb6dcc2cfc7ec704cfd2678b2816209'

json_data = requests.get(url).json()


for i in range(len(json_data['results']) - 1):
    customer_data = json_data['results'][i]
    addressList.append(customer_data['address'])
    try:
        try:
            if isinstance(int(addressList[i]['street_number']), int):
                addressStringList.append(addressList[i]['street_number'] + ' ' + addressList[i]['street_name'] + ' ' + addressList[i]['city'] +  ' ' + addressList[i]['state'])
        except:
            continue
    except:
        continue
    #addressStringList.append(string)

#for i in range(len(addressStringList)):
    #try:
     #   addressStringList[i] = addressStringList[i]
   # except:
    #    continue

print(addressStringList)
print()
print(addressList[0]['street_number'])

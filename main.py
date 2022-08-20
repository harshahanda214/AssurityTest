# importing requests and json
import requests
import json

# Getting the response from api
response = requests.get("https://api.tmsandbox.co.nz/v1/Categories/6327/Details.json?catalogue=false")
# get the response status OK or 200 of the api
response_status = response.ok
print("API response status", ";", response_status)
# Getting the dictionary from json
dict_values = response.json()
# Fetching Name
Name = dict_values['Name']
if Name == 'Carbon credits':
    print("Name", ":", Name)
else:
    False
# Fetching Canrelist
Can_relist = dict_values['CanRelist']
if Can_relist:
   print("CanRelist", ":", Can_relist)
else:
    False
# Fetching Promotions element
prom_data = dict_values['Promotions']
print(type(prom_data))
# Fetching name and description from promotions element
for i in prom_data:
    if i['Name'] == 'Gallery' and i['Description'] == 'Good position in category':
        print("Name = ", i['Name'], ",", "Description", i['Description'])


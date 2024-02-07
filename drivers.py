import json
import requests

url = f'http://ergast.com/api/f1/drivers.json?offset=0&limit=999'
response = requests.get(url).json()

with open('json data/drivers.json','w') as f:
    json.dump(response['MRData']['DriverTable']['Drivers'],f,indent=4)

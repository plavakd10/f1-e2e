import json
import requests

url = f'http://ergast.com/api/f1/circuits.json?offset=0&limit=999'
response = requests.get(url).json()

with open('json data/circuits.json','w') as f:
    json.dump(response['MRData']['CircuitTable']['Circuits'] ,f,indent=4)
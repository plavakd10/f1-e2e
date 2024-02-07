import json
import requests

url = f'http://ergast.com/api/f1/constructors.json?offset=0&limit=999'
response = requests.get(url).json()

with open('json data/constructors.json','w') as f:
    json.dump(response['MRData']['ConstructorTable']['Constructors'] ,f,indent=4)
    
   
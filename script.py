import requests
from collections import OrderedDict

url = "https://swapi.dev/api/vehicles/"
response = requests.get(url)
data = response.json()
manufacturers = OrderedDict()

for vehicle in data['results']:
    manufacturer = vehicle['manufacturer'].lower()
    manufacturers[manufacturer] = None
    
manufacturers = list(manufacturers.keys())

print("Unique manufacturers:")
for i, manufacturer in enumerate(manufacturers):
    print(f"{i+1}. {manufacturer}")
    if i == 4:
        break

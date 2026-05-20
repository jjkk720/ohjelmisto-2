import requests
import json
pyyntö = "https://api.chucknorris.io/jokes/random"
#print(pyyntö)
vitsi = requests.get(pyyntö).json()
#print(vitsi)
print(json.dumps(vitsi,indent=2))
print(vitsi["value"])
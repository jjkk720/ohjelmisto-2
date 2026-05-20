import requests

hakusana = input("Anna hakusana: ")

# Pyynnön malli: https://api.tvmaze.com/search/shows?q=girls

#muodostettiin nettiin lhetettävä pyyntö
pyyntö = "https://api.tvmaze.com/search/shows?q=" + hakusana
print("Nettiin lähtevä pyyntö:" + pyyntö)
#lähetetään nettiin GET-pyyntö, saadaan takaisin json muotoinen data
vastaus = requests.get(pyyntö).json()
print(vastaus)

#vastauksen muotoilua
#print(json.dumps(vastaus, indent=2))

#tulostetaan löytyneiden sarjojen nimet
for a in vastaus:
    print (a["show"]["name"])
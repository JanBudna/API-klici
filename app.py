import requests
import pprint

#baseUrl = "https://www.google.com/"
#klic = requests.get(baseUrl)

#print(klic) koda odgovora
#print(klic.text) #raw odgovor - t

"""
#API klic z JSON
baseUrl = "https://api.chucknorris.io/jokes/random"
for i in range(10):
    klic = requests.get(baseUrl)
    #preverimo .text, da je 100% JSON
    js = klic.json() #pretvorimo klic v dict
    #pprint.pprint(js)
    print(js.get("value"))
"""

"""
baseUrl = "https://api.nationalize.io/?name="
ime = "Jan"

klic = requests.get(baseUrl+ime).json()
#print(klic.url)
print(klic)

print(f"{klic.get("count")=}")
print(f"{klic.get("name")=}")

države = klic.get("country")


for d in države:
    print(d.get("country_id"))
    print(d.get("probability"))


#popravljen izpit
for d in države:
    print(d.get("country_id"))
    print(f"{round(d.get('probability')*100)}%")
"""

baseUrl = "https://pokeapi.co/api/v2/pokemon/"
ime = "greninja"

klic = requests.get(baseUrl+ime).json()
print(klic.get("types"))
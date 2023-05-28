import requests
import pandas as pd


urlBase='https://pokeapi.co/api/v2/'



urlView=f'{urlBase}pokemon?limit=100000&offset=0'

response = requests.get(urlView)
data=response.json()
listPokemons=data['results']
listaNEW=[]
for i,pokemon in enumerate(listPokemons):
    pokename=pokemon['name']
    listaNEW.append(pokename)
    #print(f'{i+1}-{pokename}')

print(listaNEW)
dff=pd.DataFrame(listaNEW, columns=["NOMBRE"])
print(dff)

dff.to_csv('data_1.csv')


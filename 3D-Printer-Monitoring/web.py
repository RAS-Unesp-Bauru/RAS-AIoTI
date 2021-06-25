import requests
import json

# Consumindo WebAPI

while True:
    #URL --> INSIRA O IP AQUI
    url = "IP:PORTA"

    #Buscando o URL do WebAPI
    req = requests.get(url)

    #Tentativa de acesso
    try:

        #Leitura da WebAPI
        adress_data = req.json()
        break

    except json.decoder.JSONDecodeError:
        continue

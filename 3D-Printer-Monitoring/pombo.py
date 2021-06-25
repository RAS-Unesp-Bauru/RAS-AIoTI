import json
import requests as r

class Pigeon():
    def sedex():
        # read = r.get('LINK DO SERVIDOR') #Consulta os dados inseridos no servidor
        buttom = open('hello.json','r')
        while True:
            try:
                data = json.load(buttom)
                buttom.close()
                break

            except json.decoder.JSONDecodeError:
                continue
            
        return data["inf"]

    # def on():
    #     read = open('hello.json','w')
    #     write = read.write('{"inf":true}')
    
    def off():
        read = open('hello.json','w')
        read.write('{"inf":false}')
        read.close()

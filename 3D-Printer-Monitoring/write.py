import requests as req

dado = {
  "botões": {
    "num1": "true", 
    "num2": "false",
    "time": "05:15:04"
    }
}

req = requests.Request('GET', 'http://httpbin.org/get')
req.prepare()
req.send(dado)

'''

---------- INFORMAÇÕES SOBRE A BIBLIOTECA REQUESTS -----------

BÁSICO: https://requests.readthedocs.io/pt_BR/latest/user/quickstart.html
AVANÇADO: https://requests.readthedocs.io/pt_BR/latest/user/advanced.html#advanced
PARÂMETROS + SESSION: https://requests.readthedocs.io/pt_BR/latest/api.html#sessionapi

'''
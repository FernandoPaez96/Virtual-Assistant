from bs4 import BeautifulSoup
import requests, json

code_clima = {"113" : "Soleado y despejado", "116" : "Parcialmente nublado", "119" : "Nublado", "122" : "Cielo cubierto", "143" : "Neblina", "176" : "Llubia moderada a intervalos", "179" : "Nieve moderada a intervalos", "182" : "Aguanieve moderada a intervalos", "185" : "Llovizna helada a intervalos", "200" : "Cielo tormentoso", "227" : "Chubascos de nieve", "230" : "Ventisca", "248" : "Niebla moderada", "260" :"Niebla helada", "263" : "Llovizna a intervalos", "266" : "Llovizna", "281" : "Llovizna helada", "284" : "Fuerte llovizna helada","293" : "Lluvias ligeras a intervalos", "296" : "Ligeras lluvias", "299" : "Periodos de lluvia moderada", "302" : "Lluvia moderada", "305" : "Periodos de fuertes lluvias", "308" : "Fuertes lluvias", "311" : "Ligeras lluvias heladas"}
key = "457f5097d90d51d1f92e42a7db7cfcbc"


def clima(ciudad):
    ciudad = ciudad
    url = "http://api.weatherstack.com/current?access_key={}&query={}".format(key,ciudad)
    print(url)
    req = requests.get(url)

    if req.status_code == 200:
        text = req.text
        data = json.loads(text)
        clima = data["current"]
        temperatura = clima["temperature"]
        clima_actual = str(clima["weather_code"])
        clima_actual = code_clima[clima_actual]
        climaFinal = ("La temperatura en {} es de {} grados y el clima actual es {}".format(ciudad, temperatura, clima_actual))
        return climaFinal
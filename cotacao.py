import requests



def converter_moedas(moeda_inicio,moeda_fim):
    
    link = "https://economia.awesomeapi.com.br/last/{moeda_inicio}-{moeda_fim}"


    requicição = requests.get(link)


    cotacao = requicição.json()[f"{moeda_inicio}{moeda_fim}"]["bid"]

    return cotacao



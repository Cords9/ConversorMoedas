import xmltodict

def nomes_moedas():
    with open ("moedas_disponiveis.xml" ,"+rb" ) as arquivo_moedas:
        lista_moedas = xmltodict.parse(arquivo_moedas)


    moedas = lista_moedas["xml"]
    return moedas



def conversoes():
    with open("combinacoes.xml" , "rb") as arquivo_conversoes:
        lista_conversoes = xmltodict.parse(arquivo_conversoes)



    converter = lista_conversoes["xml"]

    lista_conversoes_disponiveis= {}
    
    for conversao in converter:
        moedainicial,moedafinal = conversao.split("-")
        if moedainicial in lista_conversoes_disponiveis:
            lista_conversoes_disponiveis[moedainicial].append(moedafinal)
        else:
            lista_conversoes_disponiveis[moedainicial] = [moedafinal]
    return lista_conversoes_disponiveis
    
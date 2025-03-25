import customtkinter
from consultar_moedas import nomes_moedas, conversoes
from cotacao import cotar_moedas

# Configuração da Tela
tela = customtkinter.CTk()
tela.geometry("600x600")
tela.title("Conversor de Moedas")
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

# Funções
def converter_moedas():
    
    valor_moeda_inicial = moeda_inicial.get()
    valor_moeda_final = moeda_final.get()

    if valor_moeda_inicial and valor_moeda_final:
        valor_conversao =cotar_moedas(valor_moeda_inicial,valor_moeda_final)
        resultado_conversao.configure(text=f"1 {valor_moeda_inicial} = {valor_conversao} {valor_moeda_final}")
    
    



def carregar_moedas_finais(moeda_escolhida):
    lista_moedas_finais = conversoes_disponiveis[moeda_escolhida]
    moeda_final.configure(values=lista_moedas_finais)
    moeda_final.set(lista_moedas_finais[0])



conversoes_disponiveis = conversoes()



# Tela
titulo = customtkinter.CTkLabel(tela, text="CONVERSOR DE MOEDAS UNIVERSAL")
moeda_inicial_txt = customtkinter.CTkLabel(tela, text="Selecione a Moeda Base:")
moeda_final_txt = customtkinter.CTkLabel(tela, text="Selecione a Moeda de Conversão:")

btn_converter = customtkinter.CTkButton(tela, text="Converter", command=converter_moedas , fg_color="#0056b3",hover_color="#007BFF")

#Campos de moedas

moeda_inicial = customtkinter.CTkOptionMenu(tela, values=list(conversoes_disponiveis.keys()),command=carregar_moedas_finais)
moeda_final = customtkinter.CTkOptionMenu(tela, values=["Selecione a moeda final"])

#Campo de conversao

resultado_conversao = customtkinter.CTkLabel(tela, text="")


#Mostrar na tela
titulo.pack(padx=10, pady=10)
moeda_inicial_txt.pack(padx=10, pady=10)
moeda_inicial.pack(padx=10, pady=10)
moeda_final_txt.pack(padx=10, pady=10)
moeda_final.pack(padx=10, pady=10)
btn_converter.pack(padx=10, pady=10)
resultado_conversao.pack(padx=10, pady=10)

#Iniciar tela
tela.mainloop()

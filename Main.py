import customtkinter
from consultar_moedas import nomes_moedas

# Configuração da Tela
tela = customtkinter.CTk()
tela.geometry("600x600")
tela.title("Conversor de Moedas")
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

# Funções
def converter_moedas():
    print("Converter")

# Tela
titulo = customtkinter.CTkLabel(tela, text="CONVERSOR DE MOEDAS UNIVERSAL")
moeda_inicial_txt = customtkinter.CTkLabel(tela, text="Selecione a Moeda Base:")
moeda_final_txt = customtkinter.CTkLabel(tela, text="Selecione a Moeda de Conversão:")

btn_converter = customtkinter.CTkButton(tela, text="Converter", command=converter_moedas , fg_color="#0056b3",hover_color="#007BFF")

#Campos de moedas
moeda_inicial = customtkinter.CTkOptionMenu(tela, values=nomes_moedas)
moeda_final = customtkinter.CTkOptionMenu(tela, values=nomes_moedas)

#Mostrar na tela
titulo.pack(padx=10, pady=10)
moeda_inicial_txt.pack(padx=10, pady=10)
moeda_inicial.pack(padx=10, pady=10)
moeda_final_txt.pack(padx=10, pady=10)
moeda_final.pack(padx=10, pady=10)
btn_converter.pack(padx=10, pady=10)

#Iniciar tela
tela.mainloop()

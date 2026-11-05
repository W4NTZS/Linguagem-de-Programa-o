DOLAR = 5.43    # Dolár do dia 05/11/26

def Conversao(reais):
    conversao = reais / DOLAR
    return conversao

reais = float(input("Digite um valor em reais: R$").replace(",", "."))
print(f"R${reais:.2f} é US${Conversao(reais):.2f} em dolár".replace(".", ","))
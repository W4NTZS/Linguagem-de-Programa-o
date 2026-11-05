# Elabore um programa que receba via teclado um valor em reais e a cotação do dólar,
# calculando e apresentando o valor correspondente em dólares

DOLAR = 5.43    # cotação do dolar do dia 05/11


reais = float(input("Digite um valor em reais: R$").replace(",", "."))
conversao = reais / DOLAR

print(f"R${reais:.2f} é US${conversao:.2f} em dolár".replace(".", ","))
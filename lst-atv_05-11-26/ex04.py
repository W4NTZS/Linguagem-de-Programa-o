#Crie um programa que, a partir da digitação da quantidade de termos a serem exibidos,
# apresente na tela os n primeiros números da chamada "sequência de Fibonacci"

t1 = 0
t2 = 1
termo = int(input("Digite o termo para o fibonacci: "))
for i in range (termo):
    print(t1, end=" ")
    t1, t2 = t2, t1+t2


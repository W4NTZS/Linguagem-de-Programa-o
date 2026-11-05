fibonaccci = []
def Fibonacci(n):
    t1 = 0
    t2 = 1
    for i in range (termo):
        fibonaccci.append(t1)
        t1, t2 = t2, t1+t2

    return fibonaccci

termo = int(input("Digite a quant. de termos para o fibonacci: "))
print(Fibonacci(termo))

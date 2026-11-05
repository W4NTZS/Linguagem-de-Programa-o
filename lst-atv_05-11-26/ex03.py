#Elabore um programa que, exclusivamente com base no tempo de permanência (em minutos)
# e no tipo de veículo, calcule e apresente o valor a ser pago por um veículo em um estacionamento de acordo com a tabela abaixo.
#
#Como a tabela deixa claro, para permanências superiores a uma hora deverá ser cobrado
#  o valor correspondente a cada hora adicional ou fração, independentemente da quantidade de minutos. 
# Caso o veículo permaneça no estacionamento por 8 horas ou mais, deverá ser aplicada a tarifa especial, 
# referente a uma diária, presente na tabela, em substituição à cobrança por hora.
#              TEMPO                                     CARRO       MOTO
#              até 5 minutos                             grátis      grátis
#              primeira hora                             R$ 15,00    R$ 10,00
#              cada hora adicional ou fração             R$  7,50    R$ 5,00
#              período de 8 horas (diária)               R$ 50,00    R$ 35,00 
# ###

tarifaAdc = 0

def TarifaTempo(minutos, veiculo, tarifaAdc):
    
    tarifa = 0
    if (minutos <= 5):
        tarifa = 0
    elif (minutos == 60) and (veiculo == "CARRO"):
        tarifa = 15.00
    elif (minutos == 60) and (veiculo == "MOTO"):
        tarifa = 10.00
    elif (minutos == 480) and (veiculo == "CARRO"):
        tarifa = 50.00
    elif (minutos == 480) and (veiculo == "MOTO"):
        tarifa = 35.00
    elif minutos > 60 and veiculo == "CARRO":
        tarifa = 15 + tarifaAdc * (minutos-60)
    elif minutos > 60 and veiculo == "MOTO":
            tarifa = 10 + tarifaAdc * (minutos-60)
    elif minutos > 60 and (veiculo != "CARRO" or veiculo != "MOTO"):
        tarifa = 15 + 7.50 * (minutos - 60)
    else:
        if (veiculo == "CARRO"):
            tarifa = tarifaAdc * (minutos-5)
        if (veiculo == "MOTO"):
            tarifa =  tarifaAdc * (minutos-5)
        else:
            tarifa = 7.50 * (minutos-5)

    return f"{tarifa:.2f}"


veiculo = input("Digite o seu veiculo: ").upper()
if (veiculo == "CARRO"):
    tarifaAdc = 7.50
elif veiculo == "MOTO":
    tarifaAdc = 5.00
else:
    tarifaAdc = 7.50

minutosDePermanencia = float(input("Quanto tempo de permanencia do veiculo? (em min): "))
print(f"Tarifa de R${TarifaTempo(minutosDePermanencia, veiculo, tarifaAdc)}")
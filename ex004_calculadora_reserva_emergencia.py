#Exercício 4: Calculadora de reserva de emergência
import math

MESES_DE_RESERVA = 6

def calcular_reserva(gasto_mensal):
    return gasto_mensal * MESES_DE_RESERVA

def meses_para_juntar(reserva, aporte_mensal):
    return math.ceil(reserva / aporte_mensal)

gasto_mensal = float(input("Qual o seu gasto mensal? "))
aporte = float(input("Qual o valor que voce consegue guardar por mês? "))

reserva = calcular_reserva(gasto_mensal)
meses = meses_para_juntar(reserva, aporte)

print(f"Gasto mensal: {gasto_mensal:.2f}\nAporte: {aporte:.2f}\nSua reserva ideal é R${reserva:.2f} e você vai levar {meses} meses para juntar!")
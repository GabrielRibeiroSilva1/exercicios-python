#Exercício 2: Revisão da semana (meta: 2/10)
gastos = [38, 62, 45, 50, 71, 20, 55]
limite_diario = 50

dia = 1
total_gasto = 0
dias_acima_limite = 0

for gasto in gastos:
    if gasto <= limite_diario:
        print(f"Dia {dia}: R${gasto:.2f} ✅")
    else:
        print(f"Dia {dia}: R${gasto:.2f} ❌")
        dias_acima_limite = dias_acima_limite + 1
    total_gasto = total_gasto + gasto
    dia = dia + 1

print(f"Total gasto na semana: R${total_gasto:.2f}")
print(f"Quantidade de dias com gastos acima do limite: {dias_acima_limite}")

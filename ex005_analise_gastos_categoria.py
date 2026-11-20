#Exercício 5: Para onde vai meu dinheiro?

gastos = {
    "mercado": 850.00,
    "aluguel": 1200.00,
    "transporte": 300.00,
    "lazer": 250.00,
    "contas": 400.00,
}

def total_gastos(gastos):
    total_gasto = 0
    for categoria, valor_gasto in gastos.items():
        total_gasto += valor_gasto
    return total_gasto


total = total_gastos(gastos)
maior_gasto = 0
categoria_maior_gasto = ""

for categoria, valor in gastos.items():
    if valor >= maior_gasto:
        maior_gasto = valor
        categoria_maior_gasto = categoria
    percentual = valor / total
    if percentual > 0.3:
        print(f"{categoria}: R${valor:.2f} ({percentual:.1%}) ⚠️ {categoria} está acima de 30%")
    else:
        print(f"{categoria}: R${valor:.2f} ({percentual:.1%})")
print()
print(f"Categoria com maior gasto: {categoria_maior_gasto}")

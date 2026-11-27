gastos = [
    {"descricao": "Mercado", "categoria": "Alimentação", "valor": 320.50},
    {"descricao": "Gasolina", "categoria": "Transporte", "valor": 180.00},
    {"descricao": "Lanche", "categoria": "Alimentação", "valor": 27.90},
    {"descricao": "Internet", "categoria": "Contas", "valor": 99.90},
    {"descricao": "Uber", "categoria": "Transporte", "valor": 23.40},
    {"descricao": "Padaria", "categoria": "Alimentação", "valor": 45.00},
    {"descricao": "Luz", "categoria": "Contas", "valor": 138.20},
]

totais = {}
for gasto in gastos:
    categoria = gasto["categoria"]
    if categoria in totais:
        totais[categoria] += gasto["valor"]
    else:
        totais[categoria] = gasto["valor"]

total_geral = sum(totais.values())

for categoria, total in totais.items():
    print(f"{categoria}: R$ {total:.2f} ({total / total_geral:.1%})")
print(f"Total: R$ {total_geral:.2f}")

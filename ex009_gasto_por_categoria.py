gastos = [
    {"descricao": "Mercado", "categoria": "Alimentação", "valor": 320.50},
    {"descricao": "Gasolina", "categoria": "Transporte", "valor": 180.00},
    {"descricao": "Lanche", "categoria": "Alimentação", "valor": 27.90},
    {"descricao": "Internet", "categoria": "Contas", "valor": 99.90},
    {"descricao": "Uber", "categoria": "Transporte", "valor": 23.40},
    {"descricao": "Padaria", "categoria": "Alimentação", "valor": 45.00},
    {"descricao": "Luz", "categoria": "Contas", "valor": 138.20},
]

valor = 0
totais = {}
soma = 0
for gasto in gastos:
   
    if gasto["categoria"] in totais:
        categoria = gasto["categoria"]
        soma_valor = totais[f"{categoria}"] + gasto["valor"]
        totais[f"{categoria}"] = soma_valor
    else:
        categoria = gasto['categoria']
        totais[f"{categoria}"] = gasto["valor"]

total_geral = 0
for categoria, total in totais.items():
    total_geral += total

for categoria, total in totais.items():
    print(f"{categoria}: R$ {total:.2f} ({total/total_geral:.1%})")

print(f"Total de gastos: R$ {total_geral:.2f}")




def adicionar_gasto():
    descricao = input("Digite a descrição do gasto: ")
    valor = float(input("Digite o valor do gasto: "))
    return descricao, valor

LIMITE_DIARIO = 80
ALERTA = 0.8

def ver_resumo(gastos):
    print("Gastos do dia")
    for item in gastos:
        print(f"{item['descricao']}: R$ {item['valor']:.2f}")

    total = sum(item["valor"] for item in gastos)
    percentual = total / LIMITE_DIARIO

    print(f"Total: R$ {total:.2f} ({percentual:.1%} do limite)")
    if percentual > ALERTA:
        print("⚠️ Você passou de 80% do limite!")

def encerrar_programa():
    print("Encerrando programa")


gastos = []
lista_de_opcoes = [1, 2, 3]


while True:
    print("Menu")
    print("1 - adicionar gasto")
    print("2 - ver resumo")
    print("3 - sair")
    escolha = ""

    while escolha not in lista_de_opcoes:
        escolha = int(input("Escolha uma das opções acima: "))

    if escolha == 1:
        descricao, valor = adicionar_gasto()
        gastos.append({"descricao": descricao, "valor": valor})
        continue

    elif escolha == 2:
        ver_resumo(gastos)

    elif escolha == 3:
        encerrar_programa()
        break


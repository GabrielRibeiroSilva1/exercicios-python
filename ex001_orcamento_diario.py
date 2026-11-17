#Exercício 1: Controle do orçamento diário (meta: 1/10)
limite_diario = 50
gasto_do_dia = float(input("Digite o valor gasto hoje: "))
diferenca = limite_diario - gasto_do_dia
if diferenca >= 0:
    print("Sobrou R${:.2f}\nDentro do orçamento!".format(diferenca))
else:
    print("Excedeu R${:.2f}\nFora do orçamento!".format(diferenca * -1))
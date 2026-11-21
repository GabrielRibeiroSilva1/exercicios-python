#Execício 007 - Calculo para meta financeira
def meses_ate_meta(saldo_inicial, deposito, taxa, meta):

    depositos = 0
    mes = 1
    saldo = saldo_inicial

    while deposito <= 0:
        print("Depósito inválido! Tente com algum número maior que 0")
        deposito = float(input("Digite o valor do depósito?"))
    while saldo < meta:
        saldo = saldo * (1 + taxa)
        saldo = saldo + deposito
        depositos += deposito
        print(f"Mes {mes:02}: R${saldo:.2f}")
        mes += 1
    return saldo, mes, depositos

meta = 3000
saldo_inicial = 500
deposito = 0
taxa = 0.8 / 100

saldo, meses, depositos = meses_ate_meta(saldo_inicial, deposito, taxa, meta)

print(f"Meta batida! Seu saldo atual é R${saldo:.2f}")
print(f"Você demorou {(meses - 1)} meses para alcançar a meta!")
print(f"R${(saldo - depositos - saldo_inicial):.2f} do valor total veio apenas de rendimentos!")


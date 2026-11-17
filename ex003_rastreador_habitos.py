#Exercício 3: Rastreador de hábitos (meta: 3/10)
habitos = {
    "academia": 3,
    "leitura": 6,
    "meditação": 2,
    "água 2L": 7,
}
meta_semanal = 5
melhor_resultado_cont = 0

for habito, frequencia in habitos.items():
    if frequencia >= meta_semanal:
        print(f"{habito}: {frequencia}/7 dias ({frequencia / 7:.1%}) ✅")
    else:
        print(f"{habito}: {frequencia}/7 dias ({frequencia / 7:.1%}) ⚠️ ")
    if frequencia > melhor_resultado_cont:
        melhor_resultado_cont = frequencia
        melhor_resultado = habito

print(f"O hábito com melhor resultado foi: {melhor_resultado}")
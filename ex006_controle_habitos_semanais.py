#Exercício 6: Meu controle de hábitos da semana
semana = [
    {"dia": "segunda", "estudo_min": 90, "agua_l": 2.0},
    {"dia": "terça",   "estudo_min": 0,  "agua_l": 1.5},
    {"dia": "quarta",  "estudo_min": 75, "agua_l": 2.5},
    {"dia": "quinta",  "estudo_min": 20, "agua_l": 1.0},
    {"dia": "sexta",   "estudo_min": 45, "agua_l": 2.0},
    {"dia": "sábado",  "estudo_min": 135, "agua_l": 3.0},
    {"dia": "domingo", "estudo_min": 0,  "agua_l": 1.8},
]

def media_meta_agua(semana):
    meta_litros = 2
    dias_meta_batida = 0
    total_litros = 0
    quantidade_dias = 0

    for dicionario in semana:
        total_litros += dicionario["agua_l"]
        quantidade_dias += 1
        if dicionario["agua_l"] >= meta_litros:
            dias_meta_batida += 1
    return total_litros / quantidade_dias, dias_meta_batida

minutos_estudados = 0
qtde_dias_sem_estudo = 0
dias_sem_estudo = []

for dicionario in semana:
    minutos_estudados += (dicionario["estudo_min"])
    if dicionario["estudo_min"] == 0:
        qtde_dias_sem_estudo += 1
        dias_sem_estudo.append(dicionario["dia"])

horas_estudadas = minutos_estudados // 60
minutos_restantes = minutos_estudados % 60

media, meta_batida = media_meta_agua(semana)
print(f"Bateu a meta de 2 litros de água bebidos em {meta_batida} dias e ingeriu a média de {media:.2f}L por dia.")  
print(f"Horas estudadas: {horas_estudadas}h{minutos_restantes:02}min.")
print(f"Não estudou por {qtde_dias_sem_estudo} dias, sendo eles: {", ".join(dias_sem_estudo)}.")
def ip(registro: str) -> str:
    return registro.split()[0]

def dia(registro: str) -> str:
    return registro.split("[")[1].split(":")[0]

def ips(registros: list) -> list:
    ips_unicos = set()
    for registro in registros:
        ips_unicos.add(ip(registro))
    return list(ips_unicos)

def dia_maior_ataque(registros: list) -> list:
    frequencia_dias = {}
    for registro in registros:
        d = dia(registro)
        if d in frequencia_dias:
            frequencia_dias[d] += 1
        else:
            frequencia_dias[d] = 1

    max_ataques = max(frequencia_dias.values())
    return [dia for dia, count in frequencia_dias.items() if count == max_ataques]

def dia_menor_ataque(registros: list) -> list:
    frequencia_dias = {}
    for registro in registros:
        d = dia(registro)
        if d in frequencia_dias:
            frequencia_dias[d] += 1
        else:
            frequencia_dias[d] = 1

    min_ataques = min(frequencia_dias.values())
    return [dia for dia, count in frequencia_dias.items() if count == min_ataques]

with open("access.log", "r") as arquivo:
    registros = arquivo.readlines()

ips_unicos = ips(registros)
print(f"Quantidade de IPs diferentes detectados: {len(ips_unicos)}")

dias_maior_ataque = dia_maior_ataque(registros)
dias_menor_ataque = dia_menor_ataque(registros)

print(f"Dia(s) com maior número de ataques: {dias_maior_ataque}")
print(f"Dia(s) com menor número de ataques: {dias_menor_ataque}")

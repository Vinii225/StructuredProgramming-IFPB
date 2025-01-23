# Escreva um programa para gerar 100 números aleatórios (entre 1 e 60). Exiba
# os números que foram gerados unicamente, ou seja, não possuem repetição
# (aparecem uma única vez).

import random
numeros = [0] * 100

for i in range(100):
    numeros[i]=random.randint(1, 60)

num_no_rep=[]

for i in range(10):
    if numeros[i] not in num_no_rep:
        num_no_rep.append(numeros[i])

print(f"Números gerados: {numeros}")
print(f"Números não repetidos: {num_no_rep}")

# Ok
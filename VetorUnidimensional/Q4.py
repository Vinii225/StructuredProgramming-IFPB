# Escreva um programa para gerar 100 números aleatórios (entre 1 e 40). Entre os
# números gerados, exibir o(s) que mais se repete(m).

import random

numeros = [0] * 100
for i in range(100):
    numeros[i] = random.randint(1, 40)

numeros_repetidos=[]
numeros_freq=[0] * 100

for i in range(100):
    if numeros[i] not in numeros_repetidos:
        numeros_repetidos.append(numeros[i])
    for j in range(100):
        if numeros[i] in numeros_repetidos[i]:
            numeros_freq+=1

print(f"Os números que se repetem mais são {numeros_freq} vezes")

# RESOLVER A 4!
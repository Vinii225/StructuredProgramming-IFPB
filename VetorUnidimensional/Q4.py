# Escreva um programa para gerar 100 números aleatórios (entre 1 e 40). Entre os
# números gerados, exibir o(s) que mais se repete(m).

import random

numeros = [0] * 100
for i in range(100):
    numeros[i] = random.randint(1, 40)

numeros_repetidos=[]
count=0

for i in range(100):
    if numeros[i] not in numeros_repetidos:
       numeros_repetidos.append(numeros[i])
    elif numeros[i] in numeros_repetidos:
        count+=1

for j in range(100):
    print(f"Os números se repetem {count} vezes")
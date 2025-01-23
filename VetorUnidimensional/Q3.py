# Escreva um programa para gerar 6 números aleatórios e distintos, entre 1 e 60.

import random

numeros=[0]*6

for i in range(6):
    numeros[i]=random.randint(1, 60)
    if numeros[i]==numeros[i-1]:
        i-=1

print(f"Números aleatórios e distintos gerados: {numeros}")

# OK
# Altere a questão 3 para exibir os números ordenadamente (crescente)

import random

numeros=[0]*6

for i in range(6):
    numeros[i]=random.randint(1, 60)
    if numeros[i]==numeros[i-1]:
        i-=1

for i in range(6):
    for j in range(6):
        if numeros[i]<numeros[j]:
            aux=numeros[i]
            numeros[i]=numeros[j]
            numeros[j]=aux

print(f"Números aleatórios e distintos gerados em ordem crescente: {numeros}")

# OK
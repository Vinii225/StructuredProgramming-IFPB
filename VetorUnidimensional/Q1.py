# Escreva um programa para gerar 10 números aleatórios (entre 1 e 60). Verifique
# e exiba se existe repetição nesse vetor.

import random
numeros = [0] * 10

for i in range(10):
    numeros[i]=random.randint(1, 60)

numeros_sem_rep=[]

for i in range(10):
    if numeros[i] not in numeros_sem_rep:
        numeros_sem_rep.append(numeros[i])

print(f"Números gerados: {numeros}")

if len(numeros)==len(numeros_sem_rep):
    print("Não há repetição")
else:
    print("Há repetição")

# OK
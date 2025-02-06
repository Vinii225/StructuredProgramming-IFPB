# Escreva um programa que:
# Leia uma matriz M de ordem 20 x 50 contendo valores inteiros;
# Leia um valor inteiro K;
# Imprima todas as posições (linha e coluna) em que se encontra o valor K dentro da matriz M.

import random

M=[]

for i in range(20):
    linha=[]
    for j in range(50):
        linha.append(random.randint(0, 100))
    M.append(linha)

for linha in M:
    print(linha)

K=int(input("Digite valor para saber quantos tem na matriz: "))
count=0
for i in range(20):
    for j in range(50):
        if M[i][j]==K:
            count+=1

print(f"Há {count} número {K}")
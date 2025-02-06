# Escreva um programa que:
# Leia uma matriz quadrada de ordem 30 contendo números inteiros;
# Gere e imprima um vetor que deverá conter os elementos da diagonal principal da matriz;
# Gere e imprima um vetor que deverá conter os elementos da diagonal secundária da matriz.

import random

M=[]

for i in range(30):
    linha=[]
    for j in range(30):
        linha.append(random.randint(0, 100))
    M.append(linha)

for linha in M:
    print(linha)

d_princ=[]
for i in range(30):
    d_princ.append(M[i][i])

print("======================================================SEPARADOR=================================================================")
print(f"Diagonal Principal:", d_princ)

d_sec=[]
for i in range(30):
    d_sec.append(M[i][30-1-i])

print("======================================================SEPARADOR=================================================================")
print(f"Diagonal Secundária:", d_sec)
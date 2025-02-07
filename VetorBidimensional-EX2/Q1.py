# Uma matriz é considerada “Matriz Identidade” quando os elementos da diagonal
# principal são todos iguais a 1 (um) e os demais elementos são todos iguais a 0 (zero).
# Escreva um programa, em Python, para ler uma matriz quadrada (de ordem “N”) e
# verificar se ela é a matriz identidade.

import random

M=[]

for i in range(20):
    linha=[]
    for j in range(50):
        linha.append(random.randint(0, 100))
    M.append(linha)

for linha in M:
    print(linha)
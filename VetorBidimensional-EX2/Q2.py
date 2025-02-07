# Uma matriz é considerada “Quadrado Mágico” quando as somas dos elementos de
# cada linha, cada coluna e diagonais (principal e secundária) são todas iguais.
# Escreva um programa, em Python, para ler uma matriz quadrada (de ordem “N”) e
# verificar se ela é um quadrado mágico.

import random

linhas=[0]*4

for i in range(4):
    linhas.append(random.randint(0,10))
print(linhas)





# SOMAS DE ELEMENTOS EM CADA LINHA LINHAS
soma=0
for i in range(5):
    for j in range(5):
        soma=M[j][i]
        print(f"A linha {i} possui soma de: {soma}")
print(M)

# SOMA DE ELEMENTOS COLUNAS

# SOMA DE ELEMENTOS DIAGONAL PRINC.

# SOMA DE ELEMENTOS DIAGONAL SENC.



# Escreva um programa que:
# Leia um valor inteiro N;
# Leia um vetor A contendo N inteiros;
# Gere e imprima um vetor B onde cada elemento de B será calculado com base no elemento de A
# da mesma posição usando a seguinte regra: se o elemento de A for par, o elemento de B será 0,
# e se o elemento de A for ímpar, o elemento de B será 1.
# Exemplo: N = 8, A = [7, 12, 15, 10, 4, 9, 3, 6], B = [1, 0, 1, 0, 0, 1, 1, 0]

import random

N = int(input("Digite o valor de N: "))
A = []
B = []

for i in range(N):
    A.append(random.randint(1, 100))
    if A[i] % 2 == 0:
        B.append(0)
    else:
        B.append(1)

print(f"Lista A: {A}")
print(f"Lista B: {B}")
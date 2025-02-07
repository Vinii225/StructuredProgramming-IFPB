# Uma matriz é considerada “Matriz Simétrica” quando ela é igual à sua transposta.
# Escreva um programa, em Python, para ler uma matriz quadrada (de ordem “N”) e
# verificar se ela é uma matriz simétrica.

def eh_matriz_simetrica(matriz, n):
    for i in range(n):
        for j in range(n):
            if matriz[i][j] != matriz[j][i]:
                return False
    return True

# Leitura da matriz
n = int(input("Digite a ordem da matriz: "))
matriz = []

print("Digite os elementos da matriz linha por linha:")
for i in range(n):
    linha = list(map(int, input().split()))
    matriz.append(linha)

# Verifica se é matriz simétrica
if eh_matriz_simetrica(matriz, n):
    print("A matriz é simétrica.")
else:
    print("A matriz não é simétrica.")
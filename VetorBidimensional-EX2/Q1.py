# Uma matriz é considerada “Matriz Identidade” quando os elementos da diagonal
# principal são todos iguais a 1 (um) e os demais elementos são todos iguais a 0 (zero).
# Escreva um programa, em Python, para ler uma matriz quadrada (de ordem “N”) e
# verificar se ela é a matriz identidade.

def eh_matriz_identidade(matriz, n):
    for i in range(n):
        for j in range(n):
            if (i == j and matriz[i][j] != 1) or (i != j and matriz[i][j] != 0):
                return False
    return True

n = int(input("Digite a ordem da matriz: "))
matriz = []

print("Digite os elementos da matriz linha por linha:")
for i in range(n):
    linha = list(map(int, input().split()))
    matriz.append(linha)

if eh_matriz_identidade(matriz, n):
    print("A matriz é identidade.")
else:
    print("A matriz não é identidade.")
# Uma matriz é considerada “Quadrado Mágico” quando as somas dos elementos de
# cada linha, cada coluna e diagonais (principal e secundária) são todas iguais.
# Escreva um programa, em Python, para ler uma matriz quadrada (de ordem “N”) e
# verificar se ela é um quadrado mágico.

def eh_quadrado_magico(matriz, n):
    soma_ref = sum(matriz[0])
    
    # Verifica somas das linhas
    for linha in matriz:
        if sum(linha) != soma_ref:
            return False
    
    # Verifica somas das colunas
    for j in range(n):
        if sum(matriz[i][j] for i in range(n)) != soma_ref:
            return False
    
    # Verifica soma da diagonal principal
    if sum(matriz[i][i] for i in range(n)) != soma_ref:
        return False
    
    # Verifica soma da diagonal secundária
    if sum(matriz[i][n-i-1] for i in range(n)) != soma_ref:
        return False
    
    return True

# Leitura da matriz
n = int(input("Digite a ordem da matriz: "))
matriz = []

print("Digite os elementos da matriz linha por linha:")
for i in range(n):
    linha = list(map(int, input().split()))
    matriz.append(linha)

# Verifica se é quadrado mágico
if eh_quadrado_magico(matriz, n):
    print("A matriz é um quadrado mágico.")
else:
    print("A matriz não é um quadrado mágico.")

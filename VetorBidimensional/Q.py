# Q1 (Declarar a matriz) - OK
matriz=[[10 , 20, 30, 40], [50, 60, 70, 80], [90, 100, 110, 120]]
print(f"Matriz Inicial: {matriz}")

# Q2 (Exibir o elemento que está na linha 1 coluna 3) - OK
print(f"Matriz para exibir item (1,3): {matriz[1][3]}")

# Q3 (Alterar o elemento que está na linha 2 coluna 2 para 200) - OK
matriz[2][2]=200
print(f"Matriz para exibir matriz após multiplicação de (2,2) {matriz}")

# Q4 (Dobrar o valor dos elementos que estão na linha 2) - OK
for i in range(4):
    matriz[1][i]*=2
print(f"Matriz após multiplicar a linha 1: {matriz}")

# Q5 (Exibir a soma dos elementos que estão na linha 1) - OK
soma=matriz[1][0]+matriz[1][1]+matriz[1][2]+matriz[1][3]
print(f"Soma dos elementos na linha 1: {soma}")

# Q6 (Exibir a soma dos elementos que estão na coluna 3) - Ok
soma=matriz[0][3]+matriz[1][3]+matriz[2][3]
print(f"Soma dos elementos na coluna 3: {soma}")

# Q7 (Calcular a média de todos os elementos da matriz) - OK
soma=0
for i in range(3):
    for j in range(4):
        soma+=matriz[i][j]
        media=soma/12
print(f"A soma dos itens na matriz é {soma} e sua média {media:.2f}")

# Q8 (Adicionar uma linha na matriz com os valores: 130,140,150,160) - OK
matriz.append([130, 140, 150, 160])
print(f"Matriz após adição de nova linha: {matriz}")

# Q9 (Calcular a soma dos elementos que estão na diagonal principal) - OK
soma=0
for i in range(4):
    soma+=matriz[i][i]
print(f"Soma dos itens na diagonal (superior esquerdo para inferior direito): {soma}")

# Q10 (Calcular a quantidade de elementos da matriz que possuem valor acima da média) - OK
soma=0
count=0
for i in range(4):
    for j in range(4):
        soma+=matriz[i][j]
        media=soma/16
        if matriz[i][j]>media:
            count+=1
print(f"Quantidade de numeros maiores que a média ({media}): {count}")

print(f"Matriz final: {matriz}")
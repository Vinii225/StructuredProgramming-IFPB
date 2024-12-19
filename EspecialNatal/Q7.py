import random
# Create List
nomes=[]

# Do a loop to get names..
while True:
    nome=str(input("Digite nome: "))
    qtd=len(nome)

    if qtd!=0:
        nomes.append(nome)
    else:
        break

# Show the list
print(nomes)

# Change Random Positions from nomes
for i in range(6):
    tamanho=len(nomes)
    n1=random.randint(0, tamanho - 1)
    n2=random.randint(0, tamanho - 1)

    aux=nomes[n1]
    nomes[n1]=nomes[n2]
    nomes[n2]=aux

print(nomes)

# Sorter a name
i=random.randint(0, tamanho-1)
prox=i+1

if prox==tamanho:
    prox=0

print(i, nomes[i])
print(prox, nomes[prox])
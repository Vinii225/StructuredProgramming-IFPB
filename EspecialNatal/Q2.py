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
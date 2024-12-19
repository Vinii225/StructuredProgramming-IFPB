import random

# Create List
nomes=[]
emails=[]

# Do a loop to get names..
while True:
    nome=str(input("Digite nome: "))
    qtd=len(nome)

    if qtd!=0:
        nomes.append(nome)
    else:
        break

    email=input("email: ")
    emails.append(email)
    

# Show the list
print(nomes)
print(emails)

# Change Random Positions from nomes
for i in range(6):
    tamanho=len(nomes)
    n1=random.randint(0, tamanho - 1)
    n2=random.randint(0, tamanho - 1)

# permutar nomes
    aux=nomes[n1]
    nomes[n1]=nomes[n2]
    nomes[n2]=aux

# permutar emails
    aux=emails[n1]
    emails[n1]=emails[n2]
    emails[n2]=aux

print(nomes)
print(emails)

for i in range(tamanho):
    prox=i+1
    if prox==tamanho:
        prox=0
    print(nomes[i], nomes[prox])
    print(f"{nomes[i]} ({emails[i]}) -> {nomes[prox]} ({emails[prox]})")
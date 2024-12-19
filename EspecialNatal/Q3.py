# Create List
#nomes=[0] * 10
#
# Do a loop to get names..
#for i in range(10):
#    nomes[i]=str(input("Digite nome: "))

#copo_ajd=nomes[0]
#nomes[0]=nomes[9]
#nomes[9]=copo_ajd

# Show the list
#print(nomes)

# ---------------------------------------------------------------------------------------------------------------------------------------------------

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

# Change First to Last and Last to First
ult_ind=len(nomes)-1
aux=nomes[0]
nomes[0]=nomes[ult_ind]
nomes[ult_ind]=aux

# Show List Again
print(nomes)

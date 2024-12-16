countM=0
countF=0

countF_minus20_s=0
countM_plus30_c=0

num_pessoas=int(input("Digite quantidade de pessoas: "))
for i in range (1, num_pessoas+1):
    idade=int(input("Digite idade: "))
    genero=str(input("Digite F para feminino e M para masculino: "))
    estadocivil=str(input("Digite S para solteiro e C para casado: "))
    print(f"\n")
    if genero=="M" or genero=="m":
        countM+=1

    elif genero=="F" or genero=="f":
        countF+=1

    else:
        print("invalido") 


    if genero=="F" and idade<=20 and estadocivil=="S":
        countF_minus20_s+=1
    
    if genero=="M" and idade>30 and estadocivil=="C":
        countM_plus30_c+=1


total_h= (countM * 100) / num_pessoas
total_m= (countF * 100) / num_pessoas

print(f"Homens = {total_h:.2f} %")
print(f"Mulheres = {total_m:.2f} %")
print(f"Quantidade (Mulheres, menor ou igual a 20 anos, solteira): {countF_minus20_s}")
print(f"Quantidade (Homens, maior que 30 anos, casado): {countM_plus30_c}")

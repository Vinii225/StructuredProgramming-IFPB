num=1

somaPar=0
somaImpar=0

maior_impar=0
maior_par=0
while num!=0:
    num=int(input("Digite numero: "))

    if num % 2==0:
        somaPar+=num
        if maior_par<num:
            maior_par=num

    elif num % 2!=0:
        somaImpar+=num
        if maior_impar<num:
            maior_impar=num

print(f"Soma dos Pares: {somaPar}")
print(f"Soma dos Impares: {somaImpar}")
print(f"Maior par: {maior_par}")
print(f"Maior impar: {maior_impar}")
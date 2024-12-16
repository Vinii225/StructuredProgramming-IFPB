countf=0
precosf=0
media=0
while True: 
    valor=float(input("Digite valor: "))
    novo_valor=float(input("Digite novo valor: "))

    calculo= (novo_valor * 100) / valor
    desconto= 100 - calculo

    if desconto>0:
        print("Desconto verdadeiro achado. ")
        break

    if desconto<0:
        countf+=1
        precosf+=novo_valor
        mediaf=precosf/countf
    

print(f"Quantidade de promoções falsas: {countf}")
if media>0:
    print(f"Media de preços falso: {mediaf:.2f}")
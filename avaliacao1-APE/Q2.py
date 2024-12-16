valor=float(input("Digite valor: "))
novo_valor=float(input("Digite novo valor: "))

calculo= (novo_valor * 100) / valor
desconto= 100 - calculo

if desconto<0 or desconto==0:
    print("Desonesto")
elif desconto<=20:
    print("Honesto")
elif desconto>20 and desconto<=50:
    print("Muito Honesto")
elif desconto>50:
    print("Absurdamente Honesto")
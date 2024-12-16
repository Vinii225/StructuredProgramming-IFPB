valor=float(input("Digite valor: "))
novo_valor=float(input("Digite novo valor: "))

calculo= (novo_valor * 100) / valor
desconto= 100 - calculo

print(f"Desconto foi: {desconto:.2f} %")
count_promo=0
maior_desconto=0
promocao=0
for i in range (1, 2000001):
    valor=float(input("Digite valor: "))
    novo_valor=float(input("Digite novo valor: "))

    calculo= (novo_valor * 100) / valor
    desconto= 100 - calculo


    if desconto>0:
        count_promo+=1
        promocao= valor - novo_valor

    if promocao>maior_desconto:
        maior_desconto=promocao

print(f"Promoções verdadeiras: {count_promo}")
print(f"Maior promoção (R$): {maior_desconto:.2f}")

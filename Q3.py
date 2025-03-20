texto = "Cachorro Feliz Feliz Feliz 100"

qtd_upper = 0
qtd_lower = 0
qtd_digit = 0

for letra in texto:
    if letra.isupper():
        qtd_upper += 1
    elif letra.islower():
        qtd_lower += 1
    elif letra.isdigit():
        qtd_digit += 1

print("Quantidade de maiúscula: ", qtd_upper)
print("Quantidade de minúscula: ", qtd_lower)
print("Quantidade de números: ", qtd_digit)
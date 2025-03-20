texto = "Banana Com Chicletin 27"
novo_texto=""
for i in range(len(texto)):
    if texto[i].isdigit():
        novo_texto+="*"
    else:
        novo_texto+=texto[i]

print(novo_texto)
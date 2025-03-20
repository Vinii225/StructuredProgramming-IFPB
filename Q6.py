texto = input("Digite texto: ").strip()
palavra=["P", "y", "t", "h", "o", "n"]
contador=0

for i in range(len(texto)):
    if texto[i] in palavra:
        contador+=1

print(contador)


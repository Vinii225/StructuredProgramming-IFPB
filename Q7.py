palavras = []
while True:
    palavra = input("Digite uma palavra (ou 'fim' para terminar): ").strip()
    if palavra.lower() == "fim":
        break
    palavras.append(palavra)

contagem = {}
for palavra in palavras:
    if palavra in contagem:
        contagem[palavra] += 1
    else:
        contagem[palavra] = 1

print("Palavras distintas e suas contagens:")
for palavra, quantidade in contagem.items():
    print(f"{palavra}: {quantidade}")
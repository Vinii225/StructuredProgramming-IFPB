texto = input().strip()  
texto_normalizado = []
ultimo_espaco = True  

for caractere in texto:
    if caractere == " ":
        if not ultimo_espaco:  
            texto_normalizado.append(" ")
            ultimo_espaco = True
    else:
        texto_normalizado.append(caractere)
        ultimo_espaco = False

texto_final = "".join(texto_normalizado).rstrip()

palavras = 0
if len(texto_final) > 0:
    palavras = 1
    for c in texto_final:
        if c == " ":
            palavras += 1

print(palavras)
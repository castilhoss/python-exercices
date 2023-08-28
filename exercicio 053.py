frase = str(input("Insira uma frase: "))

for caracter in frase[::-1]:
    if caracter == " ":
        frase = (frase.replace(caracter,'')).upper()

fraseinvertida = frase[::-1]
if frase == fraseinvertida:
    print("Sua frase é um políndromo, ou seja ela pode ser lida ao contrário.")
    print(fraseinvertida)
else:
    print("Sua frase nao é um políndromo")
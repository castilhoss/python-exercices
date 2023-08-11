print("-+" * 16)
numero_1 = float(input("Insira o primeiro número: "))
print("-+" * 7)
numero_2 = float(input("Insira o segundo número: "))
print("-+" * 16)

if numero_1 > numero_2:
    print(" O PRIMEIRO valor é MAIOR!")
elif numero_2 > numero_1:
    print(" O SEGUNDO valor é MAIOR!")
elif numero_2 == numero_1:
    print("Os DOIS valores são IGUAIS!")
else:
    print("Por favor insira um valor válido")

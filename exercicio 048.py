numeros = 0
for tres in range(1,501, 2):
    if tres%3 == 0:
        numeros = numeros + tres
print("A soma de todos numéros impares multiplos de três entre 0 e 500 é {}".format(numeros))
    
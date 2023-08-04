frs = input("Insira uma frase: ")

tipo = type(frs)

print("O tipo primitivo desse valor é {}".format(tipo))

print("Só tem espaços {}".format(frs.isspace()))

print("É um número? {}".format(frs.isnumeric()))

print("É alfanúmerico? {}".format(frs.isalnum()))

print("Esta em maiuscúlas? {}".format(frs.isupper()))

print("Esta em minuscúla? {}".format(frs.islower()))

print("Esta Capitalizada? {}".format(frs.istitle()))

nome = str(input("Digite seu nome completo: "))
nome_divido = nome.split()
print("Analisando seu nome...")
print("Seu nome em maiúsculas é {}".format(nome.upper()))
print("Seu nome em minúsculas é {}".format(nome.lower()))
print("Seu nome tem ao todo {} letras".format(len(nome)))
print("Seu primeiro nome é {} e tem {} letras".format(nome_divido[0], len(nome_divido[0])))



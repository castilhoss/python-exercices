dias = float(input("Quantos dias alugados? "))
km = float(input("Quantos Km rodados? "))
valor = (dias * 60.0) + (km * 0.15)

print("O total a pagar é de R${:.2f}".format(valor))


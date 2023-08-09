numero_1 = float(input("Primeiro valor: "))
numero_2 = float(input("Segundo valor: "))
numero_3 = float(input("Terceiro valor: "))


if numero_1 > numero_2:
    numero_quasemaior = numero_1
else:
    numero_quasemaior = numero_2

if numero_quasemaior > numero_3:
    maior = numero_quasemaior
else:
    maior = numero_3

print("O maior valor digitado foi {:.0f}".format(maior))

if numero_1 > numero_2:
    quasemenor = numero_2
else:
    quasemenor = numero_1

if quasemenor < numero_3:
    menor = quasemenor
else:
    menor = numero_3
print("O menor valor digitado foi {:.0f}".format(menor))

numero = float(input("Insira um valor para ver sua tabuada: "))

for tabuada in range(1,11):
    print("{} x {} = {}".format(numero, tabuada, numero * tabuada))
    
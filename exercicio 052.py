numero = int(input("Informe um número inteiro: "))
mult = 0

for count in range(2,numero):
    if numero % count == 0:
        mult = mult+1

if  mult == 0:
    print("O número {} É primo!".format(numero))
else:
    print("O número {} NÃO é primo!".format(numero))
    
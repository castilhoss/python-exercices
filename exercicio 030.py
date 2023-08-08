import math
numero = float(input("Me diga um número qualquer: "))
calculo = numero % 2

if calculo == 0:
    print("O número {:.0f} é Par!".format(numero))
else:
    print("O número {:.0f} é Ímpar!".format(numero))

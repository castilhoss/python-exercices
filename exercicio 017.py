import math 
cateto_oposto = float(input("Comprimento do cateto oposto: "))
cateto_adjacente = float(input("Comprimento do cateto adjacente: "))
hipotenusa = math.sqrt((cateto_adjacente ** 2) + (cateto_oposto ** 2))

print("A hipotenusa vai medir {:.2f}".format(hipotenusa))

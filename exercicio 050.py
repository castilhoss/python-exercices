soma = 0
par = 0

for numb in range (1,7):
    num = int(input("Insira um valor: "))
    if num % 2 == 0:
        soma = soma + num
        par = par + 1
        
print("Os números que você informou apresentam {} números pares e a soma deles é {}.".format(par, soma))
    
    
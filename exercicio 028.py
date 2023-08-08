from random import choice
print("-=-" * 20)
print("Vou pensar em número entre 0 e 5. Tente Adivinhar...")
print("-=-" * 20)
numeros = (1, 2, 3, 4, 5)
numero = choice(numeros)
chute = int(input("Em que número eu pensei? "))

if chute == numero:
    print("Você acertou! Parabéns!!!")
else:
    print("Você errou :(, tente novamente!!)")

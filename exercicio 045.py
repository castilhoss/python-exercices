from time import sleep
import random
print("Suas opções:")
print("[ 0 ] PEDRA \n[ 1 ] PAPEL\n[ 2 ] TESOURA")
jogada = int(input("Escolha a sua jogada: "))

computador = ["Pedra", "Papel", "Tesoura"]
jogadapc = random.choice(computador)

if jogada == 0:
    escolha = "Pedra"
elif jogada == 1:
    escolha = "Papel"
elif jogada == 2:
    escolha = "Tesoura"
else:
    print("Insira um valor compatível para as jogadas!")
    quit()

    

sleep(1)
print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PO!!!")
sleep(1)
print("-=" * 12)
print("Computador jogou {}".format(jogadapc))
print("Jogador jogou {}".format(escolha))
print("-=" * 12)

if jogadapc == "Pedra" and escolha == "Papel":
    print("JOGADOR VENCE!")
elif jogadapc == "Papel" and escolha == "Pedra":
    print("COMPUTADOR VENCE!")
elif jogadapc == "Tesoura" and escolha == "Pedra":
    print("JOGADOR VENCE!")
elif jogadapc == "Pedra" and escolha == "Tesoura":
    print("COMPUTADOR VENCE!")
elif jogadapc == "Papel" and escolha == "Tesoura":
    print("JOGADOR VENCE!")
elif jogadapc == "Tesoura" and escolha == "Papel":
    print("COMPUTADOR VENCE!")
else:
    print("EMPATE!")

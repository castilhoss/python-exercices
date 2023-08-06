import random
p1 = input("Primeiro Aluno: ")
p2 = input("Segundo Aluno: ")
p3 = input("Terceiro Aluno: ")
p4 = input("Quarto aluno: ")

escolha = random.choice([p1, p2, p3, p4])

print("O Aluno escolhido foi {}".format(escolha))

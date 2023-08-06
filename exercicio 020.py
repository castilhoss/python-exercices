import random
p1 = input("Primeiro Aluno: ")
p2 = input("Segundo Aluno: ")
p3 = input("Terceiro Aluno: ")
p4 = input("Quarto aluno: ")

ordem = [p1, p2, p3, p4]

random.shuffle(ordem)

print("A ordem de apresentação será \n{}".format(ordem))


print("-+" * 10)
print("Status de Aluno")
print("-+" * 10)

nota1 = float(input("Primeira nota: "))
print("-"*5)
nota2 = float(input("Segunda nota: "))
media = (nota1 + nota2)/ 2

print("Tirando {} e {}, a média do aluno é {}".format(nota1, nota2, media))
if media < 5:
    print("Aluno Reprovado!")
elif media <= 6:
    print("Alundo está de Recuperação!")
else:
    print("Aluno está Passado!")

ano = int(input("Ano de Nascimento: "))
idade = 2023 - ano
print("O Atetla tem {} anos.".format(idade))
if idade <= 9:
    print("Classificação: MIRIM")
elif idade <= 14:
    print("Classificação: INFANTIL")
elif idade <= 19:
    print("Classificação: JÚNIR")
elif idade <= 25: 
    print("Classificação: SÊNIOR")
elif idade > 25:
    print("Classificação: MASTER")

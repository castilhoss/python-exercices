ano = int(input("Ano de Nascimento: ")) 
idade = 2023 - ano
print("Quem nasceu em {} tem {} anos em 2023".format(ano, idade))

if idade < 18:
    print("Seu alistamento séra em {}".format(ano + 18))
elif idade == 18:
    print("Você precisa se alistar IMEDIATAMENTE!")
elif idade > 18:
    print("Seu alistamento foi em {}".format(ano + 18))

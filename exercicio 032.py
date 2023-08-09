ano = float(input("Que ano quer analisar? Coloque 0 para analisar o ano atual: "))

if ano == 0:
    ano = 2023

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0: 
    print("O Ano {:.0f} é Bissexto!".format(ano))
else:
    print("O Ano {:.0f} não é Bissexto!".format(ano))

 
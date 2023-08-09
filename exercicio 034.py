salario = float(input("Qual é o seu salário do funcionário? R$"))
if salario > 1250:
    aumento = salario * 0.10
    print("Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora.".format(salario, salario + aumento))
else:
    aumentomenor = salario * 0.15
    print("Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora.".format(salario, salario + aumentomenor))

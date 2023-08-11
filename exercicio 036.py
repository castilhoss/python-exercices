print("-+-"*12)
print("Empréstimo bancário")
print("-+-"*12)

valor_casa = float(input("Qual o valor da Casa? R$"))
salario = float(input("Qual o seu salário? R$"))
anos = float(input("Em quantos anos será feito o pagamento?  "))
prestacao = valor_casa / (anos * 12)

print("Para pagar uma casa de R${:.2f} em {:.0f} anos a prestação será de R${:.2f}!".format(valor_casa, anos, prestacao))

if prestacao < salario * 0.30:
    print("Empréstimo pode ser CONCEDIDO!")
else:
    print("Empréstimo NEGADO!")


#calcule o valor da prestação mensal sabedno q ela nao pode execeder
#30% do salario ou entçao o emprestimo será negado
peso = float(input("Qual o seu peso? (Kg) "))
altura = float(input("Qual é o sua altura? (m) "))
imc = peso / (altura ** 2)
print("O seu IMC é {:.1f}.".format(imc))
if imc < 18.5:
    print("CUIDADO! Você está ABAIXO DO PESO!")
elif imc <= 25:
    print("PARABÉNS! Você está na faixa de peso NORMAL!")
elif imc < 30: 
    print("CUIDADO! Você está na faixa de SOBREPESO!")
elif imc < 40:
    print("CUIDADO! Você está na faixa de OBESIDADE!")
else:
    print("CUIDADO! Você está na faixa de OBESIDADE MÓRBIDA!")

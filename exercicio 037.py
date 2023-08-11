numero  = int(input("Digite um número inteiero: "))
texto = "Escolha uma das bases para conversão: \n[ 1 ] converter para BINÁRIO\n[ 2 ] converter para OCTAL\n[ 3 ] converter para HEXADECIMAL"
print(texto)
escolha = int(input("Sua opção: "))
if escolha == 1:
    print("O número {} convertido para BINÁRIO é igual á {}".format(numero, bin(numero)[2:]))
elif escolha == 2:
    print("O número {} convertido para OCTAL é igual á {}".format(numero, oct(numero)[2]))
elif escolha == 3:
    print("O número {} convertido para HEXADECIMAL é igual á {}".format(numero, hex(numero)[2:]))
else:
    print("Insira uma das opções válidas!")

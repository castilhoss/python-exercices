print(" ======= LOJAS CASTIELA ======= ")
preco = float(input("Preço das compras: R$"))
print("FORMAS DE PAGAMENTO")
print("[ 1 ] à vista dinheiro / cheque \n[ 2 ] à vista cartão \n[ 3 ] 2x no cartão \n[ 4 ] 3x ou mais no cartão")
forma = int(input("Qual é a opção: "))
if forma == 1:
    print("Sua compra de R${:.2f} vai custar R${:.2f} no final.".format(preco, preco * 0.90))
elif forma == 2:
    print("Sua compra de R${:.2f} vai custar R${:.2f} no final.".format(preco, preco * 0.95))
elif forma == 3:
    print("Sua compra de R${:.2f} será parcelada em 2x de R${:.2f} SEM JUROS".format(preco, preco / 2))
elif forma == 4:
    vezes = int(input("Em quantas vezes você deseja realizar o pagamento? "))
    print("Sua compra será parcelada em {:.0f}x de R${:.2f} COM JUROS DE %10.".format(vezes, (preco *1.20)/vezes))
    print("Sua compra de R${:.2f} vai custar R${:.2f} no final.".format(preco, preco * 1.20))
else:
    print("Insira uma forma de pagamento possível.")

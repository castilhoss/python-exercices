
print("="*5+" Teste de maior idade "+"="*5)

maiores = 0

for pessoas in range(1,8):
    ano = int(input("Digite o ano em que a pessoa nasceu: "))
    if ano + 18 <= 2023:
        maiores = maiores + 1

print("{} já são maiores de idade!".format(maiores))


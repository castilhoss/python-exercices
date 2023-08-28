print("="*30)
print(" "*8 +"PRODUTOR DE PA" +" "*5)
print("="*30)
numero = int(input("Informe o primeiro termo: "))
razao = int(input("Informe a razão: "))
vezes = numero + (10-1) * razao
for num in range (numero, vezes + razao, razao):
    print("{}".format(num), end="->")
    
    
print("Acabouuuuuuuuu")
    
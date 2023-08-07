nome = input("Qual é o seu nome completo? ")
nome = nome.strip()
nome = nome.lower()
print("Tem Silva no nome? {}".format('silva' in nome))

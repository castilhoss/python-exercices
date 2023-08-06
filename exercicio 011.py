larg = float(input("Largura da parede: "))
alt = float(input("Altura da parede: "))

dim = (larg * alt)
tinta = dim / 2

print("Sua parede tem a dimensão de {}x{} e sua área é de {}m². \nPara pintar essa parede, você precisará de {}L de tinta.".format(larg, alt, dim, tinta))

print("-=" * 22)
print("Analisador de Triângulos")
print("-=" * 22)
seg1 = float(input("Primeiro segmento: "))
seg2 = float(input("Segundo segmento: "))
seg3 = float(input("Terceiro segmento: "))

if (seg1 + seg2) > seg3 and (seg1 + seg3) > seg2 and (seg2 + seg3) > seg1:
    if seg1 != seg2 and seg1 != seg3 and seg2 != seg3:
        print("Os segmentos acima PODEM FORMAR um triângulo ESCALENO")
    elif seg1 == seg2 and seg1 != seg3 or seg2 == seg3 and seg2 != seg1 or seg1 == seg3 and seg1 != seg2:
        print("Os segmentos acima PODEM FORMAR um triângulo ISÓCELES")
    elif seg1 == seg2 == seg3:
        print("Os segmentos acima PODEM FORMAR um triângulo EQUILÁTERO")
else:
     print("Os segmentos acima NÃO PODEM FORMAR um triângulo")
        


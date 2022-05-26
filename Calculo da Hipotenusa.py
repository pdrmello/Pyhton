import math
print("Calculo da Hipotenusa")
co = float(input("Digite o valor do cateto oposto: "))
ca = float(input("Digite o valor do catato adjacente: "))
h = math.sqrt(math.pow(co,2) + math.pow(ca,2)) 
print(f"O resultado da hipotesnusa é {h}")
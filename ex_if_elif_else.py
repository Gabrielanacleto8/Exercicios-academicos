consumo = float(input("Digite o consumo mensal em GB: "))

if consumo <= 50:
   print("Plano básico R$ 39,90 ")
elif consumo <= 150:
   print("Plano Intermediario R$ 69,90 ")
else:
   consumo >= 150
   print("Plano premium R$ 119,90")


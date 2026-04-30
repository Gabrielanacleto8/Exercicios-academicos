litros = int(input("Informe a quantidade de litros no tanque: "))
consumo = int(input("Informe o consumo do carro  em km/l: "))
distancia = int(input("Informe o destino em km: "))

km_possivel= litros * consumo 
print(f"Voce consegue rodar {km_possivel:.2f} km ")
 
if km_possivel >= distancia:
    print("Chega até o destino ")
else:
    falta = distancia -km_possivel
    print(f"Faltam {falta:.2f} km")
    
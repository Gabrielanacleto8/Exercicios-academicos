import math

pessoas = int(input("Informe a quantidade de pessoas: "))
fatias = pessoas * 3
pizza = math.ceil(fatias / 8)

print(f"Quantidade de pizzas: {pizza}")
print(f"Quantidade de pessoas: {pessoas}")
print(f"Quantidade de fatias: {fatias}")
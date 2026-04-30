idade = [12, 17, 25, 8, 30, 15, 19, 10, 22, 14]

crianca = 0
adolescente = 0
adulto =  0

for idades in idade:
    if idades >= 18:
        adulto += 1
    elif idades >= 13:
        adolescente += 1
    else:
        crianca += 1 

print(f"Criança: {crianca}")
print(f"Adolescentes: {adolescente}")
print(f"Adulto: {adulto}")

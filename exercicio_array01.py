nota = [7.5, 4.0, 6.5, 9.0, 3.5, 5.5, 8.2, 7.0, 5.9, 6.0] 

aprovados = 0
recuperacao = 0 
reprovados = 0

for notas in nota: 
    if notas >= 7:
        aprovados += 1
    elif notas >= 5:
        recuperacao += 1
    else:
        reprovados += 1

print(f"Aprovados: {aprovados}")
print(f"Recuperação: {recuperacao}")
print(f"Reprovados: {reprovados}")

    



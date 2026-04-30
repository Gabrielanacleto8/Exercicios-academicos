sexo = input("Digite o sexo (m/f): ").upper()

while sexo not in["M", "F"]:
    print("Valor invalido! Tente novamente.")
    sexo = input("Digite o sexo (m/f): ").upper()
print("Sexo registrado com sucesso: ", sexo)

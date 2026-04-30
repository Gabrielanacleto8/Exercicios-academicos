idade = idade = int(input("Digite sua idade: "))
estudante = input("Você é estudante? (s/n): ").lower()

if idade <= 12 or idade >= 60 or estudante == 's':
    print("Meia-entrada")
else:
    print("Inteira")
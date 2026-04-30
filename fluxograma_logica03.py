idade = int(input("Digite sua idade: "))
ano_falta = 18 - idade

if idade >=18: 
    print("Pode iniciar o curso ")
else:
    print(f"Aguarde mais {ano_falta} anos para se matricular")

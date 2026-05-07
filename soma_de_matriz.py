from collections import deque 

lista = [ 
    [[1,5,9],[8,7,6],[5,4,3]],
    [[6,9,5],[8,4,2],[3,8,10]],
    [[7,5,1],[9,60,90],[80,90,7]]
]

soma = 0

for bloco in lista:
    for linha in bloco:
      for numero in linha:
        soma += numero

print(soma)
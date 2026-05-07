from collections import deque 

matriz= deque([[1,2],[3,4],[5,6],[7,8]])

multiplicacao = 1

for linha in matriz:
    for numero in linha:
        multiplicacao = multiplicacao * numero

print(multiplicacao)






    
        

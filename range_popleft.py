from collections import deque 

fila = deque(range(1,11))

while fila:
    print(fila.popleft())

from asyncio.windows_events import NULL
from random import randint

def input_matriz(n):
    matriz = []

    for r in range (n-1):
        fila = []
    
    for c in range (n-1):
        fila.append(randint(0,n^2-1))

        matriz.append(fila)
    return matriz

    if n<=0 or matriz==NULL:
        return None




            

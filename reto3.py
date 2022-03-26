from ctypes.wintypes import CHAR
import math

tabla = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
m = len(tabla)

def patron_des(letra, n):
    if type(letra) == CHAR and n>0 and n<m:

#Aplico la formula del numero de combinaciones de m elementos tomados de n en n )Sin repetición)
        m_fact =  math.factorial(m)
        
        n_fact =  math.factorial (n)

        n_m_fact = math.factorial(n-m)

        combinaciones = m_fact/n_fact * n_m_fact

    return combinaciones


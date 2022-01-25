from ast import Return
import pdb

"""
-------------------------Ejercicio 1---------------------------
pdb.set_trace()
numeros_enteros = [[2, 4, 1], [1,2,3,4,5,6,7,8], [100,250,43]]


maximo = [max(i) for i in numeros_enteros ]

print("Los numeros maximos son :", maximo)
"""

numeros = [3, 4, 8, 5, 5, 22, 13]


def es_primo(n):
    primos=[]
    if all(n%j!=0 for j in range(2,n)):
        primos.append(n)
    return primos
                
    
                
primos2 = list(filter(es_primo, numeros))    

print(primos2)


                
        




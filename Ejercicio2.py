#--------Pila---------

def factorial(lim):
    if lim == 0:
        return 1
    else:
        return lim * factorial(lim-1)

print(factorial(10))

#-------Cola--------

def factorial(lim, fact):
    if lim == 0:
        return fact
    else:
        fact *= lim
        return factorial(lim-1, fact)

print(factorial(10, 1))

"""
    1. Validar que solo entren numeros enteros.
    2. Calcular solamente el factorial de los numeros impares que estan entre 0 y el limite.*
"""

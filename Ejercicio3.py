def intercalarListas(lista1, lista2):
    if lista1 == []:
        return lista2
    else:
        return [lista1[0]] + [lista2[0]] + intercalarListas(lista1[1:], lista2[1:])

print(intercalarListas([1,3,5,7], [2,4,6,8]))

"""

    1. Optimizar para que no tenga errores por tamanos de lista.
    2. Validar que solo entren listas.
    3. Programar el mismo ejercicio con recursividad de Cola.*

"""

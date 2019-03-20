"""
    1. Programe una funcion que encuentre el valor impar mas grande dentro de una lista que entra como
        parametro.

    2. Programe una funcion que tome un string introducido por un usuario y lo escriba al reves.

    3. Programe una funcion que imprima todos los numeros dentro de una lista que son multiplos de 3.
        Tambien calcule la suma de todos estos numeros y verifique si la suma es divisible entre 6.
        (La entrada es una lista por parametro, y la salida son todos los multiplos de 3, impresos
        individualmente. Cuando se terminan de imprimir los numeros, se imprime la suma de estos)

    4. Programe una funcion que, dada una lista como parametro de entrada, escriba en otra lista todos
        los valores que estan en posiciones impares de la lista de entrada y la retorne al finalizar.

    5. Encuentre el error de la funcion dig_ab y solucionelo.
"""























def mayor(lista, num = 0):

    if lista == []:
        return num
    else:
        if lista[0] > num and lista[0]%2 != 0:
            num = lista[0]
        return mayor(lista[1:], num)


def vueltaString_aux(palabra):
    if palabra == "":
        return ""
    else:
        return palabra[-1] + vueltaString_aux(palabra[:-1])

def vueltaString():
    palabra = input()
    return vueltaString_aux(palabra)


def multDeTres(lista, res = 0):
    if lista == []:
        print(res)
        return res%6 == 0


    elif lista[0]%3 == 0:
        print(lista[0])
        res += lista[0]
        return multDeTres(lista[1:],res)

    else:
        return multDeTres(lista[1:],res)


def indImpar(lista, ind = 0):

    if ind == len(lista):
        return []
    elif ind%2 != 0:
        return [lista[ind]] + indImpar(lista, ind+1)
    else:
        return indImpar(lista, ind+1)

def dig_ab(num1, num2):

    if num1 == 0:
        return False
    elif num2 == 0:
        return True
    elif num1%10 == num2%10:
        return dig_ab(num1, num2//10)
    else:
        return dig_ab(num1//10 , num2)

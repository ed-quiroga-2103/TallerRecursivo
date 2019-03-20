def sumatoria(lim):
    if lim == 0:
        return 0
    else:
        return lim + sumatoria(lim-1)

print(sumatoria(10))


def sumatoria(lim, sum):
    if lim == 0:
        return sum
    else:
        sum += lim
        return sumatoria(lim-1, sum)

print(sumatoria(10, 0))

"""
    1. Determinar cual función es por pila y cual función es por cola.
"""

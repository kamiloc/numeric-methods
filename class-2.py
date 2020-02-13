# -*- coding: utf-8 -*-

# ---------------------------------------------------------------------
# Implementación del método de bisección y algunos casos de salida;
# Solución aproximada para f(x) entre [a,b] por el método de bisección.
#
# Entradas:
# - Función f(x)
# - [a,b] intervalo inicial
# - N número de Iteraciones
# - T criterio de convergencia
#
# Salidas:
# c valor medio de [a,b]
# ---------------------------------------------------------------------

#from math import pow, cos, sin


# Defición de la función
def f(x):
    return x**3 + x - 1


# Definición de la función 'bisección' por iteración
def biseccion(a, b, tol):
    cN, aN, bN, n = (a + b) / 2.0, a, b, 1

    while ((bN - aN) / 2.0 > tol):
        if (f(aN) * f(bN) >= 0): print("El método de bisección falló")
        elif (f(cN) == 0):
            print("La solución exacta fue encontrada {0:.3f}".format(cN))
        elif (f(aN) * f(cN) < 0):
            bN = cN
        else:
            aN = cN

        cN = (aN + bN) / 2.0
        print("n={0:.3f} cN={1:.3f} f(cN)={2:.3f}".format(n, cN, f(cN)))

    return cN


print("La solución es: {0:.3f}".format(biseccion(0, 1, 1e-3)))

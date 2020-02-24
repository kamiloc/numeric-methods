# -*- coding: utf-8 -*-

# ---------------------------------------------------------------------
# Implementación del método de newton-raphson y algunos casos de salida.
#
# Entradas:
# - Función f(x)
# - a punto inicial
# - T criterio de convergencia
#
# Salidas:
# c valor aproximado de la raiz
# ---------------------------------------------------------------------


def f(x):
    return x**3 - x**2 + 2


def df(x):
    return 3 * x**2 - 2 * x


def newton(a, tol):
    error, n = 1, 1

    while error >= tol:
        if (df(a) == 0):
            print("Derivada nula. No se puede obtener la solución")
        else:
            a_new = a - f(a) / df(a)
            error = abs(a_new - a)
            a = a_new
            n += 1

    print("La solución aproximada es: {0:.3f}".format(a))

newton(20, 1e-4)

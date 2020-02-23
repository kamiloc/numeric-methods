# -*- coding: utf-8 -*-

# ---------------------------------------------------------------------
# Taller # 1: Taller bisección
# Métodos númericos
# Autor: Cristian Camilo Barreto, Juan David Vanegas
# ---------------------------------------------------------------------

from math import e, cos, sin, tan

# Definición de la función 'bisección' por iteración
def biseccion(a, b, tol, fn, isLogInterval):
    cN, aN, bN, n = (a + b) / 2.0, a, b, 1

    while ((bN - aN) / 2.0 > tol):
        if (fn(aN) * fn(bN) >= 0):
            print("El método de bisección falló")
        elif (fn(cN) == 0):
            print("La solución exacta fue encontrada {0:.3f}".format(cN))
        elif (fn(aN) * fn(cN) < 0):
            bN = cN
        else:
            aN = cN

        cN = (aN + bN) / 2.0
        n += 1

        # Definimos si la función hace o no log por cada iteración
        if (isLogInterval):
            print("n={0:.0f} cN={1:.3f} f(cN)={2:.3f}".format(n, cN, fn(cN)))

    return cN


# Ejercicio 1
print("########### \nEjercicio #1: \n")


# Defición de la función
def fn_e1(x):
    return e**(-x - 0.7) - x - 0.7


# Por medio del método de bisección definido podemos observar que el valor para c5 es -0.156
biseccion(-1, 0, 1e-3, fn_e1, True)
print("########### \n")

# Ejercicio 2
print("########### \nEjercicio #2: \n")
tol = 1e-5


# Definicion de la función
def fn_e2_1(x):
    return cos(e**x) + x


# Implementación de la bisección
print("#-- 2.1 La solución es: {0:.3f}".format(
    biseccion(-1, 0, tol, fn_e2_1, False)))


# Definicion de la función
def fn_e2_2(x):
    return 2**x * (x - 6) - x


# Implementación de la bisección
print("#-- 2.2 La solución es: {0:.3f}".format(
    biseccion(-5, 5, tol, fn_e2_2, False)))


# Definicion de la función
def fn_e2_3(x):
    return sin(3 * x) - cos(2 * x) - 1


# Implementación de la bisección
print("#-- 2.3 La solución es: {0:.3f}".format(
    biseccion(-8, -1, tol, fn_e2_3, False)))

print("########### \n")

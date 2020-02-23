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

    # Iteramos hasta que la raiz sea exacta o dentro del valor de tolerancia
    while (abs(bN - aN) / 2.0 > tol):
        # Verificamos que el intervalo sea valido
        if (fn(aN) * fn(bN) >= 0):
            print("El método de bisección falló")
            return
        elif (fn(cN) == 0):
            print("La solución exacta fue encontrada {0:.3f}".format(cN))
            return
        # Validamos si cN esta entre a, c o c, b
        elif (fn(aN) * fn(cN) < 0):
            bN = cN
        else:
            aN = cN

        # Obtenemos nuevo valor de cN, y aumentamos el numero de iteraciones
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

# Definicion de la tolerancia = 10^(-5)
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


# Definicion de la función
def fn_e2_4(x):
    return ((e**x) / (x - 3)) + 2 * x


# Implementación de la bisección
print("#-- 2.4 La solución es: {0:.3f}".format(
    biseccion(1, 2, tol, fn_e2_4, False)))

# Definicion de la función


def fn_e2_5(x):
    return x**(-2) - tan(x)


# Implementación de la bisección
print("#-- 2.5 La solución es: {0:.3f}".format(
    biseccion(3, 4, tol, fn_e2_5, False)))

# Definicion de la función


def fn_e2_6(x):
    return x**3 - 4 * x * cos(x) + (2 * sin(x))**2 - 3


# Implementación de la bisección
print("#-- 2.6 La solución es: {0:.3f}".format(
    biseccion(-2, -1, tol, fn_e2_6, False)))

print("########### \n")

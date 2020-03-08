# -*- coding: utf-8 -*-

# ---------------------------------------------------------------------
# Primer parcial práctico
# Métodos númericos
# Autor: Cristian Camilo Barreto
# ---------------------------------------------------------------------
#
from math import cos, log, e, sin, tan, sqrt


# Definición de la función 'bisección' por iteración
def biseccion(f, a, b, tol):
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
        print("iteración={0} cN={1:.3f} f(cN)={2:.6f}".format(n, cN, f(cN)))
        n = n + 1

    return cN


## Ejercicio 01.


# Definición de la función
def f_1(x):
    return x - cos(x)


print("La solución para f(x) es: {0:.16f}".format(
    biseccion(f_1, 0.5, 1, 1e-10)))

## Ejercicio 02.


# Definición de la función 1
def f_2(x):
    return pow((x - 1), 4.5) - 5 * (x - 1) - 0.1


# Definición de la función 2
def g_2(x):
    return (x * log((x + 1))) - 2


print("La solución para f(x) es: {0:.16f}\n\n".format(
    biseccion(f_2, 1, 3, 1e-6)))
print("La solución para g(x) es: {0:.16f}".format(biseccion(g_2, 0, 2, 1e-6)))

## Ejercicio 03.


# Definición del método de Newton-Raphson
def newton(f, df, x, tol):
    error = 1
    n = 1
    while error >= tol:
        if df(x) == 0:
            print(
                "Derivada nula. La solucion no fue encontrada método newton-raphson."
            )
            return None
        else:
            h = f(x) / df(x)
            x_new = x - h
            error = abs(x_new - x)
            print("n={0:<2}, x={1:.4f}, f(x)={2:.4f}, error={3:.4f}".format(
                n, x_new, f(x_new), error))
            x = x_new
            n += 1
    print("La solución es: {0:.4f} \n\n".format(x))
    return x


# Definición de la función
def f_3(x):
    return pow(e, -x) - sin(x)


# Definición de la derivada
def df_3(x):
    return pow(e, -x) - cos(x)


newton(f_3, df_3, 2, 1e-3)

## Ejecicio 04.


# Definición del método de la secante
def secante(f, xOld, xi, tol):
    n = 1
    error = 1
    while error >= tol:
        df = (f(xOld) - f(xi)) / (xOld - xi)
        if df == 0:
            print(
                "Derivada nula. La solucion no fue encontrada por método secante."
            )
        else:
            h = f(xi) / df
            xNew = xi - h
            error = abs(xNew - xi)
            print("n={0:<2}, x={1:.4f}, f(x)={2:.4f}, error={3:.4f}".format(
                n, xNew, f(xNew), error))
            xi = xNew
            n += 1
    print("La solución es: {0:.4f} \n\n".format(xi))


# Definición de la función
def f_4(x):
    return x - (0.5 * tan(x))


secante(f_4, 1, 3.5, 1e-4)

## Ejercicio 05.


# Definición de la función
def f_5(x):
    return sqrt(10 / (x + 4))


# Definición del punto fijo
def puntoFijo(f, p0, tol, n):
    i = 1
    while i <= n:
        p = (f(p0))
        print("n={0:<2}, p={1:.6f}".format(i, p))
        if abs(p - p0) < tol:
            print("La solución es {0:.4f}".format(p))
            return None
        p0 = p
        i += 1
    print("Error: Iteraciones agotadas en el método punto fijo")


puntoFijo(f_5, 20, 1e-4, 100)

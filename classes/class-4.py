# -*- coding: utf-8 -*-

# ---------------------------------------------------------------------
# Implementación del método de secante modificada y un caso salida.
#
# Entradas:
# - Función f(x)
# - xi punto inicial
# - delta
# - T criterio de convergencia
#
# Salidas:
# c valor aproximado de la raiz
# ---------------------------------------------------------------------


def f(x):
    return x**3 - x**2 + 2


def secanteMod(xi, delta, tol):
    n = 1
    error = 1
    print("Esto es metodo de la secante modificado")
    while error >= tol:
        df = (f(xi + delta * xi) - f(xi)) / (delta * xi)
        if df == 0:
            print("Derivada nula. La solucion no fue encontrada.")
            return None
        else:
            h = f(xi) / df
            xNew = xi - h
            error = abs(xNew - xi)
            print("n={0:<2}, x={1:.4f}, f(x)={2:.4f}, error={3:.4f}".format(
                n, xNew, f(xNew), error))
            xi = xNew
            n += 1
    print("El valor de la raiz es x={0:.4f}".format(xi))
    return xi


secanteMod(-20, .1, 1e-4)

# ---------------------------------------------------------------------
# Implementación del método de punto fijo y un caso salida.
#
# Entradas:
# - Función f(x)
# - p0 punto inicial
# - T criterio de convergencia
# - n limite de iteraciones
#
# Salidas:
# c valor aproximado de la raiz
# ---------------------------------------------------------------------


def g(x):
    return x**2 - 1 / 3


def puntoFijo(f, p0, tol):
    i = 1
    error = 1
    print("Esto es metodo de punto fijo")
    while error >= tol:
        p = f(p0)
        print("n={0:<2}, p={1:.4f}, error={2:.4f}".format(i, p, error))
        error = abs(p - p0)
        p0 = p
        i += 1
    print("El valor de la raíz es: {0:.4f}".format(p))
    return


puntoFijo(g, 0.9, 1e-4)

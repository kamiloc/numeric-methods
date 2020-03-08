# -*- coding: utf-8 -*-

# ---------------------------------------------------------------------
# Taller # 2: Taller Newton-Raphson
# Métodos númericos
# Autor: Cristian Camilo Barreto, Juan David Vanegas
# ---------------------------------------------------------------------

from math import e, log

showLogs = False


def newton(f, df, xi, tol):
    error, n = 1, 1

    while error >= tol:
        if (df(xi) == 0):
            print("[Newton-Raphson]: Derivada nula. No se puede obtener la solución")
        else:
            xNew = xi - f(xi) / df(xi)
            error = abs(xNew - xi)
            if(showLogs):
                print("n={0:<2}, x={1:.4f}, error={2:.4f}".format(
                    n, xNew, error))
            xi = xNew
            n += 1

    return xi


def secante(f, xOld, xi, tol):
    error, n = 1, 1

    while error >= tol:
        df = (f(xOld)-f(xi))/(xOld-xi)
        if df == 0:
            print("[Secante]: Derivada nula. La solucion no fue encontrada.")
            return None
        else:
            h = f(xi)/df
            xNew = xi - h
            error = abs(xNew-xi)
            if(showLogs):
                print("[Secante] n={0:<2}, x={1:.4f}, f(x)={2:.4f}, error={3:.4f}".format(
                    n, xNew, f(xNew), error))
            xi = xNew
            n += 1

    return xi


# Ejercicio 1
print("########### \nEjercicio #1: \n")

# Ejercicio 1.1


def fn_1_1(x):
    return 4*pow(x, 2)-4*x*pow(e, -(2*x))+pow(e, -(4*x))


def df_1_1(x):
    return 8*x-4*(pow(e, -(2*x)-2*x*pow(e, -(2*x))))-4*pow(e, -(4*x))


print(
    "#-- 1.1 La solución aproximada es: {0:.7f}"
    .format((newton(fn_1_1, df_1_1, 1, 1e-7)))
)

# Ejercicio 1.2


def fn_1_2(x):
    return pow((x+log(x)), 2)


def df_1_2(x):
    return 2*x+((2*x+2*log(x))/x)+2*log(x)


print(
    "#-- 1.2 La solución aproximada es: {0:.7f}"
    .format((newton(fn_1_2, df_1_2, 1, 1e-7)))
)

# Ejercicio 1.3


def fn_1_3(x):
    return (pow(x, 2)/pow(e, 2))+((2*x)/e)+1


def df_1_3(x):
    return (2*x/pow(e, 2))+(2/e)


print(
    "#-- 1.3 La solución aproximada es: {0:.7f}"
    .format((newton(fn_1_3, df_1_3, -2, 1e-7)))
)

print("########### \n")


# Ejercicio 2
print("########### \nEjercicio #2: \n")


def fn_2(x):
    return pow(x, 3)-25


def df_2(x):
    return 3*pow(x, 2)


print(
    "#-- La solución aproximada es: {0:.4f}"
    .format((newton(fn_2, df_2, 2, 1e-4)))
)

print("########### \n")

# Ejercicio 3
print("########### \nEjercicio #3: \n")


def fn_3(x):
    return pow(x, 3)-(3*x)+1


print(
    "#-- La solución aproximada es: {0:.6f}"
    .format(secante(fn_3, 2, 1, 1e-6))
)

print("########### \n")

# Ejercicio 4
print("########### \nEjercicio #4: \n")

showLogs = True


def fn_4(x):
    return log(x)


def df_4(x):
    return 1/x


print(
    "#-- [Secante] La solución aproximada es: {0:.4f} \n\n"
    .format(secante(fn_4, 2.8, 2.64, 1e-4))
)

# Usando el punto incial como 2.8 la función diverge y no encuentra una solución
# para que el programa no se vea afectado se usó el punto 2.64

print(
    "#-- [Newton-Raphson] La solución aproximada es: {0:.4f} \n\n"
    .format(newton(fn_4, df_4, 2.64, 1e-4))
)

print("########### \n")

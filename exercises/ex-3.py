from math import e, log, sin, sqrt

tol, n = 1e-8, 100


def puntofijo(f, p0, tol, n):  # Método del punto fijo
    i = 1
    while i <= n:
        p = (f(p0))
        print("Iter = {0:<2}, p = {1:.8f}".format(i, p))
        if abs(p - p0) < tol:
            return p
        p0 = p
        i += 1
    print("Iteraciones agotadas: Error!")
    return


# x - e**(-x) = 0
def ejercicio1_1(x):
    return e**(-x)


print('\nEjercicio 01.1\n')
puntofijo(ejercicio1_1, -1.0, tol, n)


# x + 4 * e**(-2 * x) - 4 * log(x) = 0
def ejercicio1_2(x):
    return 4 * log(x) - 4 * e**(-2 * x)


print('\nEjercicio 01.2\n')
puntofijo(ejercicio1_2, 8, tol, n)


# x * e**(-2 * x) + sin(2 * x + 1)
def ejercicio1_3(x):
    return sin(2 * x + 1) / (-e**(-2 * x))


print('\nEjercicio 01.3\n')
puntofijo(ejercicio1_3, -0.4, tol, 5)


# 0.5 * sin(e**(-2 * x)) - x
def ejercicio1_4(x):
    return 0.5 * sin(e**(-2 * x))


print('\nEjercicio 01.4\n')
puntofijo(ejercicio1_4, 0.5, tol, n)


# x**3 - x - 10
def ejercicio1_5(x):
    return x**3 - 10


print('\nEjercicio 01.5\n')
puntofijo(ejercicio1_5, 2, tol, 4)


# e**(-x) + log(x + 8) - x**2
def ejercicio1_6(x):
    return sqrt(e**(-x) + log(x + 8))


print('\nEjercicio 01.6\n')
puntofijo(ejercicio1_6, 1, tol, n)

#Ejercicio 02


def newton(f, fprima, p0, tol, n):  # Método de Newton
    i = 1
    while i <= n:
        p = p0 - f(p0) / fprima(p0)
        print("Iter = {0:<2}, p = {1:.8f}".format(i, p))
        if abs(p - p0) < tol:
            return p
        p0 = p
        i += 1
    print("Iteraciones agotadas: Error!")
    return


def ejercicio2_f(x):
    return 3 * e**(-x) - 2 * x + log(x)


def ejercicio2_df(x):
    return -3 * e**(-x) + 1 / x - 2


def ejercicio2_g(x):  # g(x) para punto fijo
    return (3 * e**(-x) + log(x + 8)) / 2


print('\nEjercicio 02 punto fijo\n')
puntofijo(ejercicio2_g, 0.4, tol, n)

print('\nEjercicio 02 newton\n')
newton(ejercicio2_f, ejercicio2_df, 0.5, tol, n)


def ejercicio3_f(x):
    return sqrt((x + 1))


print('\nEjercicio 03\n')
puntofijo(ejercicio3_f, 1, tol, n)

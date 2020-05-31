# -*- coding: utf-8 -*-

from pprint import pprint

# 2. Implementación del método de Gauss Seidel


def distinf(x, y):
    return max([abs(x[i] - y[i]) for i in range(len(x))])


def GaussSeidel(A, b, x0, Tol, Max):
    n = len(A)
    x = [0.0 for x in range(n)]
    k = 1
    while k <= Max:
        for i in range(n):
            if abs(A[i][i]) <= 1e-15:
                print("Imposible de iterar")
                return

            s1 = sum([A[i][j] * x[j] for j in range(i)])
            s2 = sum([A[i][j] * x0[j] for j in range(i + 1, n)])
            x[i] = (b[i] - float(s1) - float(s2)) / float(A[i][i])
            x[i] = round(x[i], 1)

        print("k={0:<2}, x={1}".format(k, x))

        if distinf(x, x0) < Tol:
            print("Solución encontrada")
            return

        k += 1
        for i in range(n):
            x0[i] = x[i]

    print("Iteraciones agotadas")
    return


A = [[6, 3, 2], [1, 3, 1], [2, 1, 4]]
b = [1230, 515, 710]
x0 = [1, 1, 1]

print("Matriz A:")
pprint(A)

print("Matriz b:")
pprint(b)

print("Semilla x0:")
pprint(x0)

print("Iteracion de GaussSeidel")
GaussSeidel(A, b, x0, 5e-2, 10)

from math import sqrt

# 3. Implementación del método de Euler y RK4


def f(t, y):
    return -0.06 * sqrt(y)


def eulerMethod(a, b, y0, f, N):
    h = (b - a) / 2
    t = a
    w = y0
    print("t0 = {0:.2f}, w0 = {1:.8f}".format(t, w))
    for i in range(1, N + 1):
        w = w + h * f(t, w)
        t = a + i * h
        print("t{0:<2} = {1:.2f}, w{0:<2} = {2:.8f}".format(i, t, w))


print("Metodo de Euler")
eulerMethod(0, 1, 3, f, 113)

def RK4(a, b, y0, f, N):
    h = (b - a) / 2
    t = a
    w = y0
    print("t0 = {0:.2f}, w0 = {1:.8f}".format(t, w))
    for i in range(1, N + 1):
        k1 = h * f(t, w)
        k2 = h * f(t + h / 2, w + k1 / 2)
        k3 = h * f(t + h / 2, w + k2 / 2)
        k4 = h * f(t + h, w + k3)
        w = w + (k1 + 2 * k2 + 2 * k3 + k4) / 6
        t = a + i * h
        print("t{0:<2} = {1:.2f}, w{0:<2} = {2:.8f}".format(i, t, w))


print("Metodo de RK4:")
RK4(0, 1, 3, f, 114)

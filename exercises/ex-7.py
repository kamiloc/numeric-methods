# -*- coding: utf-8 -*-

# ---------------------------------------------------------------------
# Implementación del método de Euler y RK4
# ---------------------------------------------------------------------


def f(t, y):
    return t - t * y**2


def eulerMethod(a, b, y0, f, N):
    h = (b - a) / N
    t = a
    w = y0
    print("t0 = {0:.2f}, w0 = {1:.8f}".format(t, w))
    for i in range(1, N + 1):
        w = w + h * f(t, w)
        t = a + i * h
        print("t{0:<2} = {1:.2f}, w{0:<2} = {2:.8f}".format(i, t, w))


print("Metodo de Euler")
eulerMethod(2, 5, 0, f, 10)


def RK4(a, b, y0, f, N):
    h = (b - a) / N
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
RK4(2, 5, 0, f, 10)

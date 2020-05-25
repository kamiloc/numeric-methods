#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Implementación del método RK4

def funcionf(t, y):
    return y - t**2 + 1


def RK4(a, b, y0, f, N):
    h = (b - a) / N
    t = a
    w = y0
    print("t0={0:.4f}, w0={1:.16f}".format(t, w))
    for i in range(1, N + 1):
        k1 = h * f(t, w)
        k2 = h * f(t + h / 2, w + k1 / 2)
        k3 = h * f(t + h / 2, w + k2 / 2)
        k4 = h * f(t + h, w + k3)
        w = w + (k1 + 2 * k2 + 2 * k3 + k4) / 6
        t = a + i * h
        print("t{0:<2}={1:.4f}, w{0:<2}={2:.16f}".format(i, t, w))


print("Metodo de RK4:")
RK4(0, 2, 0.5, funcionf, 10)

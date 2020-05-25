#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Implementación del método de Euler

def funcionf(t, y):
    return y - t**2 + 1


def MEuler(a, b, y0, f, N):
    h = (b - a) / N
    t = a
    w = y0
    print("t0={0:.4f}, w0={1:.16f}".format(t, w))
    for i in range(1, N + 1):
        w = w + h * f(t, w)
        t = a + i * h
        print("t{0:<2}={1:.4f}, w{0:<2}={2:.16f}".format(i, t, w))


print("Metodo de Euler")
MEuler(0, 2, 0.5, funcionf, 10)

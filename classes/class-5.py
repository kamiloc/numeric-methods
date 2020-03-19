# -*- coding: utf-8 -*-

# ---------------------------------------------------------------------
# Implementación del método interpolador de Lagrange.
#
# Entradas:
# - Función f(x)
# - Datos de la función fData
#
# Salidas:
# c Valor de x en la función
# ---------------------------------------------------------------------


def polLagrange(data):
    def L(k, x):
        out = 1
        for i, p in enumerate(data):
            if i != k: out *= (x - p[0]) / (data[k][0] - p[0])
        return out

    def P(x):
        lag = 0
        for k, p in enumerate(data):
            lag += p[1] * L(k, x)
        return lag

    return P


fData = [(2, 1 / 2), (11 / 4, 4 / 11), (4, 1 / 4)]
polF = polLagrange(fData)

x = 3
print("El valor de la función en x={0} es: {1}".format(x, polF(x)))
# -*- coding: utf-8 -*-

# ---------------------------------------------------------------------
# Implementación del método de ajuste por mínimos cuadrados
# ---------------------------------------------------------------------


def minSqt(datos):
    N = len(datos)
    x = sum(p[0] for p in datos) / N  # x promedio
    y = sum(p[1] for p in datos) / N  # y promedio
    xx = sum(p[0]**2 for p in datos) / N  # x^2 promedio
    xy = sum(p[0]*p[1] for p in datos) / N  # x*y promedio

    def P(_x):  # Calcular los valores de 'a' y 'b' en f(_x)=a+(b*_x)
        b = float(xy-x*y) / float(xx-x**2)
        a = float(y-b*x)
        return a+b*_x

    return P


def errSqt(f, datos):
    err = sum([(p[1]-f(p[0]))**2 for p in datos])
    return err


# Datos de prueba
datos = [(-1.0, 2.0), (0.0, -1.0), (1.0, 1.0), (2.0, -2.0)]
f = minSqt(datos)

x = 1.0
print("Evaluar en x={0}: {1}".format(x, f(x)))
print("Error cuadratico: {0}".format(errSqt(f, datos)))

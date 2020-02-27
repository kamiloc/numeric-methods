from math import pi


def f(x):
    return pi * x**2 * ((9 - x) / 3) - 30


def biseccion(f, a, b, tol):
    cN, aN, bN, n = (a + b) / 2.0, a, b, 1
    error = 1
    while (error >= tol):
        if (f(aN) * f(bN) >= 0): print("El método de bisección falló")
        elif (f(cN) == 0):
            print("La solución exacta fue encontrada {0:.3f}".format(cN))
        elif (f(aN) * f(cN) < 0):
            bN = cN
        else:
            aN = cN

        cN = (aN + bN) / 2.0
        error = ((bN - aN) / bN) * 100
        print("n={0:.3f} cN={1:.3f} f(cN)={2:.3f} error={3:.3f}".format(
            n, cN, f(cN), error))

    print("La solución por bisección es: {0:.3f} \n\n".format(cN))


def falsi(f, a, b, tol):
    aN = a
    bN = b
    delta = 1
    n = 1
    while delta >= tol:
        cN = bN - (f(bN) * (bN - aN)) / (f(bN) - f(aN))
        if f(aN) * f(bN) >= 0:
            print("El metodo de falsa posición falló.")
        elif f(cN) == 0:
            print("La solucion por regla falsa es: cN={0:.16f}".format(cN))
        elif f(aN) * f(cN) < 0:
            bN = cN
        else:
            aN = cN
        cNew = bN - (f(bN) * (bN - aN)) / (f(bN) - f(aN))
        delta = ((cNew - cN) / cNew) * 100
        print("n={0:<2}, cN={1:.4f}, f(cN)={2:.4f}, delta={3:.4f}".format(
            n, cN, f(cN), delta))
        n += 1
    print("La solución regla falsa es {0:.3f}".format(cN))


biseccion(f, .5, 2.5, .5)
falsi(f, .5, 2.5, .5)

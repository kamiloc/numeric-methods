from math import pi, sqrt


def f(x):
    return pow(x, 3)-9*pow(x, 2)+(90/pi)


def df(x):
    return (3*pow(x, 2))-(18*x)


def g(x):
    return sqrt(90/(pi*(9-x)))


def biseccion(f, a, b, tol):
    cN, aN, bN, n = (a + b) / 2.0, a, b, 1
    error = 1
    while (error >= tol):
        if (f(aN) * f(bN) >= 0):
            print("El método de bisección falló")
        elif (f(cN) == 0):
            print("La solución exacta fue encontrada {0:.4f}".format(cN))
        elif (f(aN) * f(cN) < 0):
            bN = cN
        else:
            aN = cN

        cN = (aN + bN) / 2.0
        error = ((bN - aN) / bN) * 100
        print("n={0:.4f} cN={1:.4f} f(cN)={2:.4f} error={3:.4f}".format(
            n, cN, f(cN), error))

    print("La solución por bisección es: {0:.4f} \n\n".format(cN))


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
            print("La solucion por regla falsa es: cN={0:.4f} \n\n".format(cN))
        elif f(aN) * f(cN) < 0:
            bN = cN
        else:
            aN = cN
        cNew = bN - (f(bN) * (bN - aN)) / (f(bN) - f(aN))
        delta = ((cNew - cN) / cNew) * 100
        print("n={0:<2}, cN={1:.4f}, f(cN)={2:.4f}, delta={3:.4f}".format(
            n, cN, f(cN), delta))
        n += 1
    print("La solución por regla falsa es {0:.4f} \n\n".format(cN))


def secante(f, xOld, xi, tol):
    n = 1
    error = 1
    while error >= tol:
        df = (f(xOld)-f(xi))/(xOld-xi)
        if df == 0:
            print("Derivada nula. La solucion no fue encontrada por método secante.")
        else:
            h = f(xi)/df
            xNew = xi - h
            error = abs(xNew-xi)
            print("n={0:<2}, x={1:.4f}, f(x)={2:.4f}, error={3:.4f}".format(
                n, xNew, f(xNew), error))
            xi = xNew
            n += 1
    print("La solución por secante es: {0:.4f} \n\n".format(xi))


def newton(f, df, x, tol):
    error = 1
    n = 1
    while error >= tol:
        if df(x) == 0:
            print("Derivada nula. La solucion no fue encontrada método newton-raphson.")
            return None
        else:
            h = f(x)/df(x)
            x_new = x - h
            error = abs(x_new-x)
            print("n={0:<2}, x={1:.4f}, f(x)={2:.4f}, error={3:.4f}".format(
                n, x_new, f(x_new), error))
            x = x_new
            n += 1
    print("La solución por newton-raphson es: {0:.4f} \n\n".format(x))
    return x


def puntoFijo(f, p0, tol, n):
    i = 1
    while i <= n:
        p = (f(p0))
        print("n={0:<2}, p={1:.4f}".format(i, p))
        if abs(p-p0) < tol:
            print("La solución por punto fijo es {0:.4f} \n\n".format(p))
            return None
        p0 = p
        i += 1
    print("Error: Iteraciones agotadas en el método punto fijo")


biseccion(f, .5, 2.5, .05)
falsi(f, .5, 2.5, .05)
secante(f, .5, 2.5, .05)
newton(f, df, .5, .05)
puntoFijo(g, 1, .05, 15)

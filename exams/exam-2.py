def polLagrange(data):
    def L(k, x):
        out = 1
        for i, p in enumerate(data):
            if i != k:
                out *= (x - p[0]) / (data[k][0] - p[0])
        return out

    def P(x):
        lag = 0
        for k, p in enumerate(data):
            lag += p[1] * L(k, x)
        return lag

    return P


def PolNewton(datos):
    n = len(datos) - 1
    F = [[0 for x in datos] for x in datos]

    for i, p in enumerate(datos):
        F[i][0] = p[1]

    for i in range(1, n + 1):
        for j in range(1, i + 1):
            F[i][j] = (F[i][j - 1] - F[i - 1][j - 1]) / \
                (datos[i][0] - datos[i - j][0])

    def L(k, x):
        out = 1

        for i, p in enumerate(datos):
            if (i <= k):
                out *= (x - p[0])
        return out

    def P(x):
        newton = F[0][0]
        for i in range(1, n + 1):
            newton += F[i][i] * L(i - 1, x)
        return newton

    return F, P


polData = [(0.5, -0.69314), (0.8, -0.22314), (1.4, 0.33647),
           (1.6, 0.47), (1.8, 0.58778), (2.0, 0.69314)]
polF = polLagrange(polData)
Tab, Pol = PolNewton(polData)

""" x = 2.71828
print("[Lagrange] El valor de la función en x={0} es: {1}".format(x, polF(x)))
print("[Newton] El valor de la función en x={0} es: {1}".format(x, Pol(x))) """


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
datos = [(2, 5), (7, 9), (11, 14), (15, 21)]
f = minSqt(datos)

x = 20
print("Evaluar en x={0}: {1}".format(x, f(x)))
print("Error cuadratico: {0}".format(errSqt(f, datos)))


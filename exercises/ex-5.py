from pprint import pprint


def PolNewton(datos):
    n = len(datos) - 1
    F = [[0 for x in datos] for x in datos]

    for i, p in enumerate(datos):
        F[i][0] = p[1]

    for i in range(1, n + 1):
        for j in range(1, i + 1):
            F[i][j] = (F[i][j - 1] - F[i - 1][j - 1]) / (datos[i][0] - datos[i - j][0])

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


testData = [(-1, 4), (2, 7), (1, 10), (-2, 31)]
Tab, Pol = PolNewton(testData)

print("\nTabla de diferencias divididas:")
pprint(Tab)

xVal = 3
print("\nPolinomio evaluado en x={0}:".format(xVal))
pprint(Pol(xVal))

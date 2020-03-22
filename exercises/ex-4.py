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


fData = [(0.5, -0.69314), (0.8, -0.22314), (1.2, 0.18232), (1.4, 0.33647),
         (1.6, 0.47000), (1.8, 0.58778), (2.0, 0.69314)]
polF = polLagrange(fData)

x = 1
print("El valor de la función en x={0} es: {1}".format(x, polF(x)))

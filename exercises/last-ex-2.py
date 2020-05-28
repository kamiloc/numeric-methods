def RectaMinSq(datos):
    X = sum([p[0] for p in datos])
    Y = sum([p[1] for p in datos])
    XX = sum([(p[0])**2 for p in datos])
    XY = sum([p[0]*p[1] for p in datos])
    m = len(datos)

    def P(x):  # recta de mínimos cuadrados
        a0 = float(Y*XX-X*XY)/float(m*XX-X**2)
        a1 = float(m*XY-X*Y)/float(m*XX-X**2)
        return a0+a1*x
    return P


def ErrorSq(f, datos):  # Error cuadrático
    E = sum([(p[1]-f(p[0]))**2 for p in datos])
    return E


# datos de prueba
datos = [(1, 150), (15, 580), (56, 1125), (90, 1630), (115, 1945), (150, 2430)]
f = RectaMinSq(datos)
print("Evaluar en x=1:")
print(f(1.0))
print(r"Error cuadr\'atico:")
print(ErrorSq(f, datos))  # calcular error cuadrático)
print("\n")

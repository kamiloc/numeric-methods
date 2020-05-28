from pprint import pprint

def distinf(x, y):
    return max([abs(x[i] - y[i]) for i in range(len(x))])


def jacobi(A, b, x0, Tol, Max):
    n = len(A)  # definimos el tamaño del sistema de ecuaciones
    x = [0.0 for x in range(n)]  # llenamos la matriz de ceros
    k = 1  # contador
    while k <= Max:
        for i in range(n):
            if abs(A[i][i]) <= 1e-15:
                print("Improsible de iterar")
                return
            s = sum([A[i][j] * x0[j] for j in range(n) if j != i])
            x[i] = (b[i]-float(s)) / float(A[i][i])
        print(k)
        pprint(x)
        if distinf(x, x0) < Tol:
            print("Solucion encontrada")
            return
        k += 1
        for i in range(n):
            x0[i] = x[i]
    print("iteraciones agotadas")
    return


A = [[1, 0, 0, 0, 1, 0],
     [0, 1, 0, 0, 0, 0],
     [0, 0, 1, 0, 0, 0],
     [0, 0, 1, -1, 0, -1],
     [0, 0, 0, 1, 1, 0],
     [1, -1, 0, 0, 0, 1]]
b = [600, 701, -1, -800, 600, 100]
x0 = [1, 1, 1, 1, 1, 1]
print("Matriz A:")
pprint(A)
print("Matriz b:")
pprint(b)
print("Semilla x0:")
pprint(x0)
print("Iteracion de jacobi")
jacobi(A, b, x0, 1e1, 10)

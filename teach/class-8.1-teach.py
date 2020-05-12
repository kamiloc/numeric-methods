from pprint import pprint


def distinf(x, y):
    return max([abs(x[i] - y[i]) for i in range(len(x))])


def GaussSeidel(A, b, x0, Tol, Max):
    n = len(A)  #Definimos el tamaño del sistema de ecuaciones
    x = [0.0 for x in range(n)]  #Llenamos la matriz x con ceros
    k = 1  #Colocamos un contador
    while k <= Max:
        for i in range(n):
            if abs(A[i][i]) <= 1e-15:
                print("imposible de iterar")
                return
            s1 = sum([A[i][j] * x[j] for j in range(i)])
            s2 = sum([A[i][j] * x0[j] for j in range(i + 1, n)])
            x[i] = (b[i] - float(s1) - float(s2)) / float(A[i][i])
        #print(k)
        #pprint(x)
        print("k={0:<2}, x={1:.16f}".format(k, x))
        if distinf(x, x0) < Tol:
            print("Solucion encontrada")
            return
        k += 1
        for i in range(n):
            x0[i] = x[i]
    print("Iteraciones agotadas")
    return


A = [[10, -1, 2], [-1, 11, -1], [2, -1, 10]]
b = [6, 25, -11]
x0 = [0, 0, 0]

print("Matriz A:")
pprint(A)

print("Matriz b:")
pprint(b)

print("Semilla x0:")
pprint(x0)

print("Iteracion de GaussSeidel")
GaussSeidel(A, b, x0, 1e-4, 50)  #Tol=10^(-4) y Max=50

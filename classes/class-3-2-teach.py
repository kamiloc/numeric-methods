from math import *

def f(x): 
    return x**3 - x**2 + 2

def secante(x_old,xi,tol):
    n=1
    error=1
    print("Esto es metodo de la secante")
    while error >= tol:
        df=(f(x_old)-f(xi))/(x_old-xi)
        if df == 0:
            print("Derivada nula. La solucion no fue encontrada.")
            return None
        else:
            h = f(xi)/df 
            # x(i+1) = x(i) - f(x) / f'(x) 
            x_new = xi - h
            error = abs(x_new-xi)
            print("n={0:<2}, x={1:.4f}, f(x)={2:.4f}, error={3:.4f}".format(n, x_new, f(x_new), error))
            xi = x_new
            n+=1
    print("El valor de la raiz es x={0:.4f}".format(xi))
    return xi

x0 = -20 # Valor incial
xi = -10
tol = 1e-4
secante(x0,xi,tol)
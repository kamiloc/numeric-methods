 '''Solución aproximada para f(x)=0 usando el metodo de Newton Raphson.

    Parametros
    ----------
    f : Funcion f(x) a la cual se les busca la solucion a la ecuación f(x)=0.
    df: Derivada de f(x).
    x0 : Valor inicial para la solución de f(x)=0.
    tol : Criterio de convergencia (error porcentual)

    Salidas
    -------
    h : Valor numerico para el cociente entre f(x)/df(x)
    x_new : Valor numerico que surge de la implementación del metodo de Newton-Raphson
        x_new = x - h
        Continua el proceso hasta que error < tol y devuelve x_new.
        Si df(x) == 0, no regresa nada.
'''

from math import *

def f(x): 
    return x**3 - x**2 + 2
  
# Derivative of the above function  
# which is 3*x^x - 2*x 
def df(x): 
    return 3*x**2 - 2*x 
  
# Function to find the root 
def newton(x,tol): 
    error = 1
    n=1
    print("Este es el metodo de Newton-Raphson")
    while error >= tol:
        if df(x) == 0:
            print("Derivada nula. La solucion no fue encontrada.")
            return None
        else:
            h = f(x)/df(x) 
            # x(i+1) = x(i) - f(x) / f'(x) 
            x_new = x - h
            error = abs(x_new-x)
            print("n={0:<2}, x={1:.4f}, f(x)={2:.4f}, error={3:.4f}".format(n, x_new, f(x_new), error))
            x = x_new
            n+=1
    print("El valor de la raiz es x={0:.4f}".format(x))
    return x

x0 = -20 # Valor incial
tol = 1e-4
newton(x0,tol)
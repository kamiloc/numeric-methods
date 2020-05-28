def f(x):
    return (pow(20, 2)*(3+x))/(9.8*pow(((3*x)+(pow(x, 2)/2)), 3))-1

# Derivative of the function


def df(x):
    return -((16000*(pow((5*x), 2)+(30*x)+54))/((49*pow(x, 4)) * pow((x+6), 4)))

# Function to find the root


def newton(x, tol):
    error = 1
    n = 1
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
            print("n={0:<2}, x={1:.4f}, f(x)={2:.4f}, error={3:.4f}".format(
                n, x_new, f(x_new), error))
            x = x_new
            n += 1
    print("El valor de la raiz es x={0:.4f}".format(x))
    return x


x0 = 1  # Valor incial
tol = 0.001
newton(x0, tol)

# -*- coding: utf-8 -*-

# ---------------------------------------------------------------------
# Compendio de programas.
# Matemáticas para Ingeniería. Métodos numéricos con Python.
# Copyright (C) 2020 Los autores del texto.
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>
# ---------------------------------------------------------------------

# Implementación del método de bisección y algunos casos de salida.

from math import *


def pol(x):
    return x**3+4*x**2-10  # retorna $pol(x)=x^3+4x^2-10$


def trig(x):
    return x*cos(x-1)-sin(x)  # retorna $trig(x)=x\cos(x-1)-\sin(x)$


def pote(x):  # retorna $pote(x)=7^x-13$
    return pow(7, x)-13


def bisec(f, a, b, tol, n):  # Método de bisección
    i = 1
    while i <= n:
        p = a+(b-a)/2
        print("i = {0:<2}, p={1:.16f}".format(i, p))
        if abs(f(p)) <= 1e-15 or (b-a)/2 < tol:
            return p
        i += 1
        if f(a)*f(p) > 0:
            a = p
        else:
            b = p
    print("Iteraciones agotadas: Error!")
    return

# $pol(x)$, $a = 1$, $b = 2$, $Tol = 10^{-8}$, $N_0 = 100$
print("\n"+r"-- Bisecci\'on funci\'on pol(x):"+"\n")
bisec(pol, 1, 2, 1e-8, 100)

# $trig(x)$, $a = 4$, $b = 6$, $Tol = 10^{-8}$, $N_0 = 100$
print("\n"+r"-- Bisecci\'on funci\'on trig(x):"+"\n")
bisec(trig, 4, 6, 1e-8, 100)

# $pote(x)$, $a = 0$, $b = 2$, $Tol = 10^{-8}$, $N_0 = 100$
print("\n"+r"-- Bisecci\'on funci\'on pote(x):"+"\n")
bisec(pote, 0, 2, 1e-8, 100)

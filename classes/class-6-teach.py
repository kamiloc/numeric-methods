#!/usr/bin/env python3
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

# Implementación del interpolador de Newton y algunos casos de salida.

from math import *
from pprint import pprint


def NewtonPol(dat):
    n = len(dat) - 1
    F = [[0 for x in dat] for x in dat]  # crear tabla nula

    for i, p in enumerate(dat):  # condiciones iniciales
        F[i][0] = p[1]

    for i in range(1, n + 1):  # tabla de diferencias divididas
        for j in range(1, i + 1):
            F[i][j] = (F[i][j - 1] - F[i - 1][j - 1]) / (
                dat[i][0] - dat[i - j][0])

    def L(k, x):  # polinomio $L_k(x)=\prod\limits_{i \leq k}(x-x_i)$
        out = 1
        for i, p in enumerate(dat):
            if i <= k:
                out *= (x - p[0])
        return out

    def P(x):  # $P(x)=f[x_0]+\sum_{k=1}^{n}f[x_0,x_1,\ldots,x_k]L_{k-1}(x)$
        newt = 0
        for i in range(1, n + 1):
            newt += F[i][i] * L(i - 1, x)
        return newt + F[0][0]

    return F, P


datost = [(-1, 3), (0, -4), (1, 5), (2, -6)]
T, P = NewtonPol(datost)
print("\nTabla de diferencias divididas:")
pprint(T)
print("\nEvaluar el polinomio en x=0")
print(P(0))

datosf = [(2, 1 / 2), (11 / 4, 4 / 11), (4, 1 / 4)]
T, P = NewtonPol(datosf)
print("\nTabla de diferencias divididas:")
pprint(T)
print("\nEvaluar el polinomio en x=3")
print(P(3))

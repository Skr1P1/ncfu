#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

x = float(input('Введите числ х -->'))
k = int(input('Введите числ k -->'))
n = int(input('Введите числ n -->'))
eps = 1e-10

while math.fabs(x) > eps:
    a = (x*x/4)**k
    b = math.factorial(k)*(math.factorial(k+n))
    k+=1
print(((x/2)**n)*a/b)


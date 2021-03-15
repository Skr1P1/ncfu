#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math
import sys

EPS = 1e-10
if __name__ == '__main__':
    x = int(input("Введите x "))
    n = int(input('Введите n'))
    if x == 0:
        print("Неверное значение х", file=sys.stderr)
        exit(1)
    a = x
    S, k = a, 1
    while math.fabs(a) > EPS:
        a *= (((x**2/4)**k)/math.factorial(k)*(math.factorial(k+n)))
        S += a
        k += 1
        break
# Вывести значение функции.
    print(((x/2)**n)*a)



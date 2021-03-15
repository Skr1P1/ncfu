#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

a = int(input('Введите сторону a -->'))
b = int(input('Введите сторону b -->'))
c = int(input('Введите сторону c -->'))

if a > 0 and b > 0 and c > 0:
    if a + b > c or a + c > b or b + c > a:
        if a == b or a == c or c == b:
            print('Этот треугольник равнобедренный')
        if a == b == c:
            print('Этот треугольник равносторонний')
        if a != b !=c:
            print('Этот треугольник разносторонний')
    else:
        print('Треугольник построить не возможно')
else:
    print('Треугольник построить не возможно')
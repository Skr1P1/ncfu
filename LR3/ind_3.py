#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

k = int(input('Введите число -->'))
l = int(math.sqrt(k))

for i in range(2, l):
    if k % i == 0:
        print(0)
        quit()
    i += 1
print(1)
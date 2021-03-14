#!/usr/bin/env python3
# -*- coding: utf-8 -*-

k = int(input('Введите число k -->'))


def index():
    for i in range(10, 99):
        a = i // 10
        b = i % 10
        if k == b or k == a:
            ind = i - 10
            print(ind, end=' ')


def num():
    for i in range(10, 99):
        a = i // 10
        b = i % 10
        if k == b or k == a:
            print(i, end=' ')


def honest():
    x = []
    for i in range(10, 99):
        a = i // 10
        b = i % 10
        x.append(a)
        x.append(b)
    print(x[k - 1])


index()
print('\n')
num()
print('\n')
honest()









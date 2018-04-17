""" Short functions to help w/ Project Euler.
"""
from __future__ import division

import os
import sys
import math
import operator as op


def is_prime(number):
    if number > 1:
        if number == 2:
            return True
        if number % 2 == 0:
            return False
        for current in range(3, int(math.sqrt(number) + 1), 2):
            if number % current == 0:
                return False
        return True
    return False

def primefactorization(number):
    if number == 1:
        return
    for x in get_prime():
        if x > math.sqrt(number):
            pf = [number]
            break
        if number % x == 0:
            pf = [x] + primefactorization(int(number / x))
            break
    return pf

def ncr(n, r):
    r = min(r, n-r)
    if r == 0:
        return 1
    numer = reduce(op.mul, xrange(n, n-r, -1))
    denom = reduce(op.mul, xrange(1, r+1))
    return numer//denom

def get_prime():
    x = 2 
    yield x
    x = 3
    while True:
        if is_prime(x):
            yield x
        x += 2

def get_fib():
    a, b = 1, 2
    while True:
        yield a
        a, b = b, a+b

def get_trinum():
    x = 1
    while True:
        yield (x * (x+1) / 2)
        x += 1

def get_odd(initial=1):
    while True:
        yield initial
        initial += 2

def get_even(initial=2):
    while True:
        yield initial
        initial += 2

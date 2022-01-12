#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
from funkcje import power_mod
from funkcje import xgcd
from funkcje import modinv
"""

def power_mod(x, k, p=None):		# x^k jeżeli p=None lub x^k mod p jeżeli p =/= None
    b = bin(k).lstrip('0b')
    r = 1

    for i in b:
        r = r**2

        if i == '1':
            r = r * x

        if p:
            r %= p

    return r


def xgcd(b, a):
	x0, x1, y0, y1 = 1, 0, 0, 1
	while a != 0:
		q, b, a = b // a, a, b % a
		x0, x1 = x1, x0 - q * x1
		y0, y1 = y1, y0 - q * y1
	return  b, x0, y0


def modinv(a, m):
	g, x, y = xgcd(a, m)
	return x % m

#!/usr/bin/env python
# -*- coding: utf-8 -*-

from generuj_pierwsze import generuj_pierwsze as genpierw
from funkcje import xgcd


def RSA_keygen(bity):
	p = genpierw(bity,1)[0]
	q = genpierw(bity,1)[0]

	print "p = ",p
	print "q = ",q

	n = p * q

	print "n = ",n

	nEuler = (p - 1) * (q - 1)

	print "Funkcja eulera dla n przyjmuje wartość: ", nEuler

	while True:
		e = genpierw(bity,1)[0]
		nwd, s, t = xgcd(nEuler, e)
		if nwd == (s*nEuler + t*e):
			d = t % nEuler
			break
			
	print "Publiczny (n,e): ", (n,e)
	print "Prywatny (n,d): ", (n,d)
			
	return (n,e), (n,d)


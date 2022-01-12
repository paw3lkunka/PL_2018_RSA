#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import random
import math
import sys
import getopt
from funkcje import power_mod

############################################

def test_pierwszosci_rabina(p, s=5):

    if p == 2:						# jeśli dwójka	
        return True

    if not (p & 1):					# nieparzysta
        return False



    tmp = p - 1
    u = 0
    r = tmp  						# p-1 = 2**u * r

    while r % 2 == 0:				# dopóki r parzyste
        r >>= 1						# przesuwa r o bit w prawo
        u += 1

    assert p-1 == 2**u * r			# warunek



    def czy_swiadek(a):				# czy liczba a ma świadka pierwszości
        z = power_mod(a, r, p)		# z = a^r mod p

        if z == 1:
            return False

        for i in range(u):
            z = power_mod(a, 2**i * r, p)

            if z == tmp:
                return False

        return True


    for j in range(s):
        a = random.randrange(2, p-2)

        if czy_swiadek(a):
            return False
    
    return True

###############################################

def generuj_pierwsze(n=512, k=1):
    assert k > 0
    assert n > 0 and n < 4096
    
    x = random.getrandbits(n)
    pierwsze = []
    
    while k>0:
        if test_pierwszosci_rabina(x, s=7):
            pierwsze.append(x)
            k = k-1

        x = x+1
		
    return pierwsze

################################################


if __name__ == "__main__":
	argv = sys.argv[1:]
	
	try:
		opts, args = getopt.getopt(argv, "c:b:", ["ilosc", "bity"])
	except getopt.GetoptError as err:
		print(err)
		opts = []
	
	n = 1024
	k = 2
	
	for opt, arg in opts:
		if opt in ["-c", "ilosc"]:
			k = int(arg)
		if opt in ["-b", "bity"]:
			n = int(arg)
			
	pierwsze = generuj_pierwsze(n,k)
	
	print(pierwsze)


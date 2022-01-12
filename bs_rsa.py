#!/usr/bin/env python
# -*- coding: utf-8 -*-

from generuj_pierwsze import generuj_pierwsze as genpierw
from generuj_pierwsze import power_mod

from rsa_keygen import RSA_keygen

from funkcje import power_mod
from funkcje import xgcd
from funkcje import modinv

import sys
import getopt
	
#######################################

def zaciemn(m, k, public):
	n, e = public
	return power_mod(power_mod(m,1,n) * power_mod(k, e, n), 1, n)

def zaciemn_string(m, k, public):
	mPrim = []
	
	for c in m:
		mPrim.append(zaciemn(ord(c), k, public))
		
	return mPrim

##############################

def generuj_podpis(mPrim, private):
	n, d = private
	sPrim = []
	
	for c in mPrim:
		sPrim.append(power_mod(c, d, n))
		
	return sPrim

##############################

def zdejmij_zaciemnienie(sPrim, k, n):
	s = []
	for c in sPrim:
		s.append(power_mod(c*modinv(k, n), 1, n))
	
	return s

##############################

def sprawdz_podpis(m, s, private):
	n, e = private
	for i in range(len(s)):
		a = int( s[i] )
		b = power_mod(ord(m[i]), e, n)
		
		if a !=	b:
			return False
			
	return True

###################################################


if __name__ == "__main__":
	argv = sys.argv[1:]
	
	try:
		opts, args = getopt.getopt(argv, "m:f:u:r:s:b:CSKh", ["message=", "message_file=", "public_key_file=", "private_key_file=", "signature_file=", "bits=", "check", "sign", "keygen", "help"])
	except getopt.GetoptError as err:
		print(err)
		opts = []
	
	m = None
	u = None
	r = None
	sf = None
	bits = None
	
	for opt, arg in opts:
		if opt in ["-m", "--message="]:
			m = arg
			mf = raw_input("W celu zachowania wiadomości podaj nazwę pliku (messages/): ")
			with open("messages/"+mf, 'w') as mes_file:
				mes_file.write(m)
		if opt in ["-f", "--message_file="]:
			with open("messages/"+arg, 'r') as mes_file:
				m=mes_file.read()
		
		if opt in ["-u", "--public_key_file="]:
			u = arg
		if opt in ["-r", "--private_key_file="]:
			r = arg
		if opt in ["-s", "--signature_file="]:
			sf = arg
		if opt in ["-b", "--bits"]:
			bits = int(arg)
		if opt in ["-h", "--help"]:
			with open("README.txt", 'r') as help_file:
				tmp = help_file.read()
			print tmp
			sys.exit()
			
			
	
	for opt,arg in opts:		
		if opt in ["-K", "--keygen"]:
			if not bits:
				bits = input("Ilość bitów p i q: ")
			public, private = RSA_keygen(bits)
			if not u:
				u = raw_input("Nazwa pliku do zapisania klucza publicznego (public_keys/): ")
			with open("public_keys/"+u, 'w') as public_file:
				public_file.write("%s\n" % str(public[0]))
				public_file.write("%s\n" % str(public[1]))
			if not r:
				r = raw_input("Nazwa pliku do zapisania klucza prywatnego (private_keys/): ")
			with open("private_keys/"+r, 'w') as private_file:
				private_file.write("%s\n" % str(private[0]))
				private_file.write("%s\n" % str(private[1]))
						
		elif opt in ["-S", "--sign"]:
			# zaciemniajacy
			if not m:
				m = raw_input("Podaj wiadomość do zaciemnienia: ")
				mf = raw_input("W celu zachowania wiadomości podaj nazwę pliku (messages/): ")
				with open("messages/"+mf, 'w') as mes_file:
					mes_file.write(m)
				
			if not u:
				u = raw_input("Plik do odczytania klucza publicznego (public_keys/): ")
			with open("public_keys/"+u, 'r') as public_file:
				n = int(public_file.readline().replace('\n',''))
				e = int(public_file.readline().replace('\n',''))
			publiczny = (n, e)	
			
			if not bits:
				bits = input("Ilość bitów losowej liczby do zaciemniania wiadomości:")
			
			k = genpierw(bits, 1)[0]
			assert k < n
			
			print "k = ",k
			
			mPrim = zaciemn_string(m, k, publiczny)
			print "Zaciemniona wiadomosc m: ",mPrim
			
			# podpisujący
			if not r:
				r = raw_input("Plik do odczytania klucza prywatnego (private_keys/): ")
			with open("private_keys/"+r, 'r') as public_file:
				n = int(public_file.readline().replace('\n',''))
				d = int(public_file.readline().replace('\n',''))
			prywatny = (n, d)
				
			sPrim = generuj_podpis(mPrim, prywatny)	
			print "Zaciemniony podpis : ", sPrim
			
			#zaciemniający
			s = zdejmij_zaciemnienie(sPrim, k, n)
			print "Podpis: ", s
			
			if not sf:
				sf = raw_input("Nazwa pliku do zapisania podpisu (signatures/): ")
			with open("signatures/"+sf, 'w') as sign_file:
				for item in s:
					sign_file.write("%s\n" % item)
			
			break
			
		elif opt in ["-C", "--check"]:
			if not m:
				mf = raw_input("Plik z wiadomością (messages/): ")
				with open("messages/"+mf, 'r') as mes_file:
					m = mes_file.read()
			
			if not sf:
				sf = raw_input("Plik do odczytania podpisu (signatures/): ")
			with open("signatures/"+sf, 'r') as sign_file:
				s = sign_file.readlines()
				
			if not r:
				r = raw_input("Plik do odczytania klucza prywatnego (private_keys/): ")
			with open("private_keys/"+r, 'r') as public_file:
				n = int(public_file.readline().replace('\n',''))
				d = int(public_file.readline().replace('\n',''))
			prywatny = (n, d)
			
			if sprawdz_podpis(m, s, prywatny):
				print "Podpis się zgodził!"
			else:
				print "Brak zgodności podpisu!"
				
			break
			

	if not len(opts):
		print "Wybierz opcję -h lub --help by nauczyć się korzystać z programu :)"
	


# PŁ Kryptografia 2018 -> RSA

RSA keys generator and signing tool made by myself during cryptography course.

bs_rsa.py

[ OPIS ]

Program generuję klucze algorytmu RSA, tworzy ślepe podpisy w oparciu o RSA, potrafi sprawdzić autentyczność ślepego podpisu.
Proszę nie stosować go w sposób niewskazany gdyż może być to działanie niesatysfakcjonujące, niepełne.

W przypadku niepodania odpowiedniej liczby argumentów program zapyta o nie sam interaktywnie. 
Wszystkie pliki wykorzystywane do działania muszą znaleźć sie w odpowiednich folderach:

/messages		-> pliki wiadomości
/signatures		-> pliki podpisów
/public_keys	-> pliki kluczy publicznych
/private_keys	-> pliki kluczy prywatnych

Przy odczytywaniu/zapisywaniu podajemy jedynie nazwę PLIKU TEKSTOWEGO. Nie całą ścieżkę.

[ TRYBY DZIAŁANIA ]

-h, --help	

-> pokaż tą notatkę
------------------------------------------------------------

-C, --check	

->sprawdź autentyczność podpisu: 

$ ./bs_rsa.py -C (-m WIADOMOŚĆ | -f PLIK_M , -s PLIK_S , -r PLIK_R)
 
Zwróci stosowny komunikat czy dla wiadomości WIADOMOŚĆ lub treści PLIK_M , podpis z pliku PLIK_S jest autentyczny z wykorzystaniem klucza prywatnego z pliku PLIK_R.	
------------------------------------------------------------

-S, --sign

-> stwórz podpis ślepy

$ ./bs_rsa.py -S (-m WIADOMOŚĆ | -f PLIK_M , -u PLIK_U , -r PLIK_R , -s PLIK_S , -b BITY)

Dla wiadomości WIADOMOŚĆ lub treści PLIK_M oraz kluczy publicznego w PLIK_U i prywatnego w PLIK_R tworzy podpis ślepy w pliku PLIK_S. 
BITY to ilość bitów w losowej liczbie k służącej do zaciemniania i zdejmowania zaciemnienia.
------------------------------------------------------------	

-K, --keygen

-> generuje klucze publiczne i prywatne RSA

$ ./bs_rsa.py -K (-b BITY , -u PLIK_U , -r PLIK_R)

BITY - ilość bitów w liczbach pierwszych p i q. Tworzy klucz publiczny w pliku PLIK_U oraz prywatny w pliku PLIK_R.
------------------------------------------------------------

[ OPCJE ]

-m, --message=				-> treść wiadomości ( użyj " " )
-f, --message_file=			-> nazwa pliku z treścią wiadomości
-u, --public_key_file=		-> nazwa pliku z kluczem publicznym
-r, --private_key_file=		-> nazwa pliku z kluczem prywatnym
-s, --signature_file=		-> nazwa pliku z podpisem ślepym
-b, --bits=					-> ilość bitów do zastosowania w generowaniu liczb pierwszych


[ AUTORZY ]

WFTIMS Politechnika Łódzka 2018/2019

Piotr Ruciński		216878
Andrzej Miszczak 	216841
Paweł Kunka			216819


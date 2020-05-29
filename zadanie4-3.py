import string
import math
plik = open("sygnaly.txt").read().split()
check = 0
alfabet = list(string.ascii_letters)
for x in plik:
    suma = 0
    for z in x:
        for i,y in enumerate(x):
            nuwka = int(alfabet.index(z)) - int(alfabet.index(x[i]))
            nuwka = math.fabs(nuwka)
            if nuwka > 10:
                suma = 1
    if suma == 0:
        print(x)
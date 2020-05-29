plik = open("sygnaly.txt").read().split()
counter = 0
licznik = 0
rozw = ""
for i,x in enumerate(plik):
    slowo = []
    for z in x:
        cnt = 0
        for y in slowo:
            if y == z:
                cnt = cnt + 1
        if cnt == 0:
            slowo.append(z)
    if len(slowo) > licznik:
        licznik = len(slowo)
        rozw = plik[i]

print(rozw+" "+str(licznik))
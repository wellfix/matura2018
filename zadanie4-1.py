plik = open("sygnaly.txt").read().split()
counter = 0
slowo = ""
for x in plik:
    counter = counter + 1
    if counter == 40:
        slowo = slowo + x[9]
        counter = 0
print(slowo)
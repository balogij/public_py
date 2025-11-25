class Allatfaj:

    def __init__(self, fajnev, tomeg):
        self.fajnev = fajnev
        self.tomeg = tomeg


#main
allatfajok = []
for _ in range(3):
    hiba = False
    fajnev = ""
    tomeg = 0
    while (not hiba):
        try:
            fajnev = input("Add meg egy állatfaj nevét!")
            hiba = True
        except ValueError:
            print("Ez nem szöveg!")

    hiba = False
    while (not hiba):
        try:
            tomeg = int(input("Hány kilogramm a tömege egy példánynak?"))
            hiba = True
        except ValueError:
            print("Ez nem szám!")

    allat = Allatfaj(fajnev, tomeg)
    allatfajok.append(allat)

max_ind = len(allatfajok)
lehnehezebballat = allatfajok[0]
for i in range(max_ind):
    if allatfajok[i].tomeg > lehnehezebballat.tomeg:
        lehnehezebballat = allatfajok[i]

print(f"A(z) {lehnehezebballat.fajnev}, a legnehezebb")
target_file = open("legnehezebb.txt", "w")
print(f"A(z) {lehnehezebballat.fajnev}, a legnehezebb", file=target_file)

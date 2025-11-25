class Allatfaj:
    def __init__(self,fajnev,tomeg):
        self.fajnev = fajnev
        self.tomeg = tomeg

#main
allatfajok = []
for _ in range(3):
    szoveg = False
    szam = False
    fajnev = ""
    tomeg = 0
    while(not szoveg):
        try:
            fajnev = input("Add meg egy állatfaj nevét:")
            szoveg = True
        except Exception:
            print("Ez nem szöveg!")

    while(not szam):
        try:
            tomeg = int(input("Add meg az állatfaj tömegét:"))
            szam = True
        except ValueError:
            print("Ez nem szám!")
    
    allat = Allatfaj(fajnev, tomeg)
    allatfajok.append(allat)

max_ind = len(allatfajok)
for i in range(max_ind):
    print(f"Állatfaj: {allatfajok[i].fajnev}, Tömeg: {allatfajok[i].tomeg}")

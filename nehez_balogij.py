class Allatfaj:
    def __init__(self,fajnev,tomeg):
        self.fajnev = fajnev
        self.tomeg = tomeg

#main
allatfajok = []
for _ in range(3):
    szoveg = False
    szam = False
    allat = Allatfaj
    while(not szoveg):
        try:
            allat.fajnev = input("Add meg egy állatfaj nevét:")
            szoveg = True
        except:
            print("Ez nem szöveg!")

    while(not szam):
        try:
            allat.tomeg = input("Add meg egy állatfaj nevét:")
            szam = True
        except:
            print("Ez nem szám!")
            
    allatfajok.append(allat)
max_ind = len(allatfajok)
for i in range(max_ind):
    print(allatfajok[i])
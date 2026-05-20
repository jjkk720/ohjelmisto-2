#Kirjoita Auto-luokka, jonka ominaisuuksina ovat rekisteritunnus, huippunopeus,
#tämänhetkinen nopeus ja kuljettu matka. Kirjoita luokkaan alustaja,
#joka asettaa ominaisuuksista kaksi ensin mainittua parametreina saatuihin arvoihin.
#Uuden auton nopeus ja kuljetut matka on asetettava automaattisesti nollaksi. Kirjoita pääohjelma,
#jossa luot uuden auton (rekisteritunnus ABC-123, huippunopeus 142 km/h).
#Tulosta pääohjelmassa sen jälkeen luodun auton kaikki ominaisuudet.

#VALMIS

class Auto:

    nopeusnyt = 0
    matka = 0

    def __init__(self, rekisteri, huippunop):
        self.rekisteri = rekisteri
        self.huippunop = huippunop

auto1 = Auto("ABC-123", "142km/h")

print(f"Auton\n -rekisteri on {auto1.rekisteri} \n -huippunopeus on {auto1.huippunop} \n -tämänhetkinen nopeus on {Auto.nopeusnyt} \n -kuljettu matka on {Auto.matka}. ")




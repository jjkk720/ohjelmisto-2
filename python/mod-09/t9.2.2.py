#Jatka ohjelmaa kirjoittamalla Auto-luokkaan kiihdytä-metodi,
#joka saa parametrinaan nopeuden muutoksen (km/h). Jos nopeuden muutos on negatiivinen,
#auto hidastaa. Metodin on muutettava auto-olion nopeus-ominaisuuden arvoa.
#Auton nopeus ei saa kasvaa huippunopeutta suuremmaksi eikä alentua nollaa pienemmäksi.
#Jatka pääohjelmaa siten,
#että auton nopeutta nostetaan ensin +30 km/h, sitten +70 km/h ja lopuksi +50 km/h.
#Tulosta tämän jälkeen auton nopeus. Tee sitten hätäjarrutus määräämällä nopeuden muutos -200 km/h
#ja tulosta uusi nopeus.
#Kuljettua matkaa ei tarvitse vielä päivittää.

#VALMIS


class Auto:

    #nopeusnyt = 0
    #matka = 0

    def __init__(self, rekisteri, huippunop):
        self.rekisteri = rekisteri
        self.huippunop = huippunop
        self.nopeusnyt = 0
        self.matka = 0

    def kiihdytä(self, nopeuden_muutos):
        self.nopeusnyt = self.nopeusnyt + nopeuden_muutos
        if self.nopeusnyt + nopeuden_muutos <0:
            self.nopeusnyt = 0


auto1 = Auto("ABC-123", "142km/h")


print(f"Auton\n -rekisteri on {auto1.rekisteri} \n -huippunopeus on {auto1.huippunop} \n -tämänhetkinen nopeus on {auto1.nopeusnyt} \n -kuljettu matka on {auto1.matka}. ")

auto1.kiihdytä(30)
print(f"Auton {auto1.rekisteri} nopeus on nyt {auto1.nopeusnyt}km/h.")
auto1.kiihdytä(70)
print(f"Auton {auto1.rekisteri} nopeus on nyt {auto1.nopeusnyt}km/h.")
auto1.kiihdytä(50)

print(f"Auton {auto1.rekisteri} nopeus on nyt {auto1.nopeusnyt}km/h.")

print("Hätäjarrutus")
auto1.kiihdytä(-200)
print(f"Auton {auto1.rekisteri} nopeus on nyt {auto1.nopeusnyt}km/h.")



#def kiihdytä(self, nopeuden_muutos):
    #for i in range(nopeuden_muutos):
     #   self.nopeusnyt + 1
    #print(self.nopeusnyt)


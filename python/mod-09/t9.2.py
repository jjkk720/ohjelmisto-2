#Jatka ohjelmaa kirjoittamalla Auto-luokkaan kiihdytä-metodi,
#joka saa parametrinaan nopeuden muutoksen (km/h).
#Jos nopeuden muutos on negatiivinen, auto hidastaa.
# Metodin on muutettava auto-olion nopeus-ominaisuuden arvoa.
# Auton nopeus ei saa kasvaa huippunopeutta suuremmaksi eikä alentua nollaa pienemmäksi.
# Jatka pääohjelmaa siten, että auton nopeutta nostetaan ensin +30 km/h,
# sitten +70 km/h ja lopuksi +50 km/h. Tulosta tämän jälkeen auton nopeus.
# Tee sitten hätäjarrutus määräämällä nopeuden muutos -200 km/h ja tulosta uusi nopeus.
#Kuljettua matkaa ei tarvitse vielä päivittää.



class Auto:
    def __init__(self, rekisteri, huippunopeus, nopeusnyt=0, matka=0, nopeuden_muutos=0):
        self.rekisteri = rekisteri
        self.huippunopeus = huippunopeus
        self.nopeusnyt = nopeusnyt
        self.matka = matka
        #self.nmuutos = nopeuden_muutos

    def kiihdytä(self, nopeuden_muutos):
        return auto1.nopeusnyt + nopeuden_muutos





auto1 = Auto("ABC-123", "142 km/h")
#auto2 = Auto("DEF-456", "200 km/h", "50 km/h", "1000 km" )
print(f"Auton 1 \n-rekisterinumero on {auto1.rekisteri}\n-huippunopeus on {auto1.huippunopeus} \n-tämänhetkinen nopeus on {auto1.nopeusnyt}\n-kuljettu matka on {auto1.matka}.")
#print(f"Auton 2 \n-rekisterinumero on {auto2.rekisteri}\n-huippunopeus on {auto2.huippunopeus} \n-tämänhetkinen nopeus on {auto2.nopeusnyt}\n-kuljettu matka on {auto2.matka}.")

auto1.kiihdytä(30)

auto1 = Auto("ABC-123", "142 km/h", )

print(f"Auton 1 \n-rekisterinumero on {auto1.rekisteri}\n-huippunopeus on {auto1.huippunopeus} \n-tämänhetkinen nopeus on {auto1.nopeusnyt} km/h\n-kuljettu matka on {auto1.matka}.")
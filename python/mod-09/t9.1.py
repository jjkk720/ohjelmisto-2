class Auto:
    def __init__(self, rekisteri, huippunopeus, nopeusnyt=0, matka=0):
        self.rekisteri = rekisteri
        self.huippunopeus = huippunopeus
        self.nopeusnyt = nopeusnyt
        self.matka = matka

auto1 = Auto("ABC-123", "142 km/h")
print(f"Auton \n-rekisterinumero on {auto1.rekisteri}\n-huippunopeus on {auto1.huippunopeus} \n-tämänhetkinen nopeus on {auto1.nopeusnyt}\n-kuljettu matka on {auto1.matka}.")


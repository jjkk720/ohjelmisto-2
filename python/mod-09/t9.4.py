
#Nyt ohjelmoidaan autokilpailu. Uuden auton kuljettu matka alustetaan automaattisesti nollaksi.
#Tee pääohjelman alussa lista,
#joka koostuu kymmenestä toistorakenteella luodusta auto-oliosta.
#Jokaisen auton huippunopeus arvotaan 100 km/h ja 200 km/h väliltä.
#Rekisteritunnus luodaan seuraavasti “ABC-1”, “ABC-2” jne. Sitten kilpailu alkaa.
#Kilpailun aikana tehdään tunnin välein seuraavat toimenpiteet:

#Jokaisen auton nopeutta muutetaan siten,
#että nopeuden muutos arvotaan väliltä -10 ja +15 km/h väliltä.
#Tämä tehdään kutsumalla kiihdytä-metodia.
#Kaikkia autoja käsketään liikkumaan yhden tunnin ajan.
#Tämä tehdään kutsumalla kulje-metodia.
#Kilpailu jatkuu, kunnes jokin autoista on edennyt vähintään 10000 kilometriä.
#Lopuksi tulostetaan kunkin auton kaikki ominaisuudet selkeäksi taulukoksi muotoiltuna.


import random
autot =[]
class Auto:
    tehty= 0


    def __init__(self, rekisteri= 0+1, huippunop = random.randint(100,200)):
        self.rekisteri = rekisteri
        self.huippunop = huippunop
        self.nopeusnyt = 0
        self.matka = 0
        Auto.tehty = Auto.tehty + 1
        autot.append

    def kiihdytä(self, nopeuden_muutos):
        self.nopeusnyt = self.nopeusnyt + nopeuden_muutos
        if self.nopeusnyt + nopeuden_muutos <0:
            self.nopeusnyt = 0

    def kulje(self, tuntimäärä):
        self.matka = self.matka + tuntimäärä * self.nopeusnyt





for i in range(10):
    auto = "auto"+str(1)
    autot.append(auto)
#auto1 = Auto("ABC-123", "142km/h")
print([autot])
print(Auto.tehty)

#print(f"Auton\n -rekisteri on {auto1.rekisteri} \n -huippunopeus on {auto1.huippunop} \n -tämänhetkinen nopeus on {auto1.nopeusnyt} \n -kuljettu matka on {auto1.matka}. ")

#auto1.kiihdytä(30)
#print(f"Auton {auto1.rekisteri} nopeus on nyt {auto1.nopeusnyt}km/h.")
#auto1.kiihdytä(70)
#print(f"Auton {auto1.rekisteri} nopeus on nyt {auto1.nopeusnyt}km/h.")
#auto1.kiihdytä(50)

#print(f"Auton {auto1.rekisteri} nopeus on nyt {auto1.nopeusnyt}km/h.")

#print("Hätäjarrutus")
#auto1.kiihdytä(-200)
#print(f"Auton {auto1.rekisteri} nopeus on nyt {auto1.nopeusnyt}km/h.")

#auto1.kiihdytä(60)
#print(f"Auton {auto1.rekisteri} nopeus on nyt {auto1.nopeusnyt}km/h.")

#auto1.kulje(1.5)
#print(f"Auton {auto1.rekisteri} kulkema matka on nyt {auto1.matka}km")

#auto1.kulje(1)
#print(f"Auton {auto1.rekisteri} kulkema matka on nyt {auto1.matka}km")

#auto1.kulje(5.7)
#print(f"Auton {auto1.rekisteri} kulkema matka on nyt {auto1.matka}km")

#auto1.kiihdytä(20)
#print(f"Auton {auto1.rekisteri} nopeus on nyt {auto1.nopeusnyt}km/h.")
#auto1.kulje(2.2)
#print(f"Auton {auto1.rekisteri} kulkema matka on nyt {auto1.matka}km")
#Laajenna ohjelmaa siten, että mukana on kulje-metodi,
#joka saa parametrinaan tuntimäärän.
#Metodi kasvattaa kuljettua matkaa sen verran kuin auto on tasaisella
#vauhdilla annetussa tuntimäärässä edennyt.
#Esimerkki: auto-olion tämänhetkinen kuljettu matka on 2000 km. Nopeus on 60 km/h.
#Metodikutsu auto.kulje(1.5) kasvattaa kuljetun matkan lukemaan 2090 km.





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

    def kulje(self, tuntimäärä):
        self.matka = self.matka + tuntimäärä * self.nopeusnyt





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

auto1.kiihdytä(60)
print(f"Auton {auto1.rekisteri} nopeus on nyt {auto1.nopeusnyt}km/h.")

auto1.kulje(1.5)
print(f"Auton {auto1.rekisteri} kulkema matka on nyt {auto1.matka}km")

auto1.kulje(1)
print(f"Auton {auto1.rekisteri} kulkema matka on nyt {auto1.matka}km")

auto1.kulje(5.7)
print(f"Auton {auto1.rekisteri} kulkema matka on nyt {auto1.matka}km")

auto1.kiihdytä(20)
print(f"Auton {auto1.rekisteri} nopeus on nyt {auto1.nopeusnyt}km/h.")
auto1.kulje(2.2)
print(f"Auton {auto1.rekisteri} kulkema matka on nyt {auto1.matka}km")
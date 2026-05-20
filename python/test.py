class Koira:
    def __init__(self, nimi, syntymävuosi, haukahdus="Vuh-vuh"):
        self.nimi = nimi
        self.syntymävuosi = syntymävuosi
        self.haukahdus = haukahdus

    def hauku(self, kerrat):
        for i in range(kerrat):
            print(self.haukahdus)
        return


koira1 = Koira("Muro", 2018)
koira2 = Koira("Rekku", 2022, "Viu viu viu")
koira3 =Koira("Musti",2019,"Hau-Hau")

koira1.hauku(2)
koira2.hauku(5)
koira3.hauku(9)



class Koira:

    tehty = 0

    def __init__(self, nimi, syntymävuosi, haukahdus="Vuh-vuh"):
        self.nimi = nimi
        self.syntymävuosi = syntymävuosi
        self.haukahdus = haukahdus
        Koira.tehty = Koira.tehty + 1

koira1 = Koira("Muro", 2018)
koira2 = Koira("Rekku", 2022, "Viu viu viu")
print ("Koiria on nyt {Koira.tehty}.")

print("kertolasku{2*2}")
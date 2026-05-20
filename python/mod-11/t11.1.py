class Julkaisu:
    def __init__(self, nimi):
        self.nimi = nimi

    def tulosta(self):
        print(f"nimi{self.nimi}")


class Kirja:
    def __init__(self, kirjoittaja, sivumäärä):
        self.kirjoittaja= kirjoittaja
        self.sivumäärä=sivumäärä


class Lehti:
    def __init__(self,päätoimittaja):
        self.päätoimittaja= päätoimittaja


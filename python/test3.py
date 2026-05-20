class Työntekijä:

    työntekijöiden_lukumäärä = 0

    def __init__(self, etunimi, sukunimi):
        Työntekijä.työntekijöiden_lukumäärä = Työntekijä.työntekijöiden_lukumäärä + 1
        self.työntekijänumero = Työntekijä.työntekijöiden_lukumäärä
        self.etunimi = etunimi
        self.sukunimi = sukunimi
        self.liittymispäivämäärä = 6+1

    def tulosta_tiedot(self):
        print(f"{self.työntekijänumero}: {self.etunimi} {self.sukunimi} {self.liittymispäivämäärä}")

työntekijät = []
työntekijät.append(Työntekijä("Kale","Vala"))
työntekijät.append(Työntekijä("Viivi", "Virta"))
työntekijät.append(Työntekijä("Ahmed", "Habib"))
työntekijät.append(Työntekijä("Nakke", "Nakuttaja"))

for e in työntekijät:
    e.tulosta_tiedot()
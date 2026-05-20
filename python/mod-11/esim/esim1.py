class Polkupyörä:
    def __init__(self, merkki, vaihteiden_lkm):
        self.merkki = merkki
        self.vaihteiden_lkm= vaihteiden_lkm

    def tulosta(self):
        print("Polkupyörän tiedot:")
        print(f"Polkupyörän merkki: {self.merkki}")
        print(f"Vaihteiden määrä: {self.vaihteiden_lkm}")
        return
class Sähköpyörä(Polkupyörä):
    def __init__(self, merkki , vaihteiden_lkm, omistaja, toimintasäde):
        #kutsutaan yliluokan (Polkupyörä) alustajaa
        super().__init__(merkki, vaihteiden_lkm)
        #lisätään omat (Sähköpolkupyrä) ominaisuudet
        self.omistaja = omistaja
        self.toimintasäde = toimintasäde

    def tulosta(self):
        #'ylikirjoitetaan' yliluokan metodi
        # hyödynnetään yliluokan valmista toimintoa
        super().tulosta()
        #tulostetaan lisäksi puuttuvat tiedot
        print(f"omistaja: {self.omistaja}")
        print(f"toimintasäde: {self.toimintasäde}")



#Pääohjelma
eka_pyörä = Polkupyörä("Helkama", "3")
eka_pyörä.tulosta()

toka_pyörä = Sähköpyörä("Tunturi", 4, "Mie", 40)
toka_pyörä.tulosta()
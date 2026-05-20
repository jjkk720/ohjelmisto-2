"""
Koodaa Kissa-luokka.
Kissa-luokalla on 2 ominaisuutta: nimi ja rotu.
Jos köyttäjä ei anna kissalle rodun nimeä, niin se saa arvoksi "kotikissa".
Tee luokalle alustaja, jossa voidaan antaa luotavan olion arvot.
Luo pääohjelmassa 2 kissaa: eka kissan rotuna on 'Ragdoll',
toiselle ei määritetä rotua.
Tulosta molempien kissojen kaikki ominaisuudet.
"""

kissannimi = input("Anna kissan nimi")

class Kissa:
    def __init__(self, nimi, rotu="kotikissa"):
        self.nimi = nimi
        self.rotu = rotu

kissa1 = Kissa(kissannimi, "Ragdoll")
kissa2 = Kissa("joku",)

print(f"Kissan nimi on {kissa1.nimi}")

class Kissae:
    def __init__(self, nimi, rotu="kotikissa"):
        self.nimi = nimi
        #huom. parametrin nimi on eri luokan ominaisuus
        self.rotu = rotu

kissa3 = Kissae("Miska", "Ragdoll")
kissa4 = Kissae("Minni",)

#tulostetaan molempien kissojen kaikki arvot

print(f"Nimi:{kissa3.nimi} on {kissa3.rotu}")
print(f"Nimi:{kissa4.nimi} on {kissa4.rotu}")




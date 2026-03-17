import random
from abc import ABC, abstractmethod

# Programmis on kasutatud 4 POOP põhimõtet:
# Abstraktsioon, Pärilus, Polümorfism, Kapseldamine


# Abstraktne baasklass
class Tegelane(ABC):

    def __init__(self, nimi, elu):
        self.nimi = nimi
        self._elu = elu  # kapseldamine

    # abstraktne meetod
    @abstractmethod
    def ründa(self, vastane):
        pass

    # ühine meetod kõigile tegelastele
    def võta_kahju(self, kahju):
        self._elu -= kahju

        # elu ei tohi minna alla 0
        if self._elu < 0:
            self._elu = 0

        print(self.nimi, "sai", kahju, "kahju. Elu alles:", self._elu)

    def on_elus(self):
        return self._elu > 0


# Sõdalane pärib Tegelane klassist
class Sõdalane(Tegelane):

    # polümorfism - iga klass teeb rünnaku erinevalt
    def ründa(self, vastane):
        kahju = random.randint(10, 20)
        print(self.nimi, "lööb mõõgaga!")
        vastane.võta_kahju(kahju)


# Maag pärib samuti Tegelane klassist
class Maag(Tegelane):

    def __init__(self, nimi, elu, mana):
        super().__init__(nimi, elu)
        self._mana = mana  # kapseldamine

    def ründa(self, vastane):

        if self._mana >= 10:
            kahju = random.randint(15, 25)
            self._mana -= 10
            print(self.nimi, "kasutab loitsu. Mana alles:", self._mana)
            vastane.võta_kahju(kahju)
        else:
            print(self.nimi, "ei saa rünnata, mana on otsas")


# Vibukütt klass
class Vibukütt(Tegelane):

    def __init__(self, nimi, elu, nooled):
        super().__init__(nimi, elu)
        self._nooled = nooled

    def ründa(self, vastane):

        if self._nooled > 0:
            kahju = random.randint(8, 18)
            self._nooled -= 1
            print(self.nimi, "laseb noole. Nooli alles:", self._nooled)
            vastane.võta_kahju(kahju)
        else:
            print(self.nimi, "ei saa rünnata, nooled on otsas")


# lahingu funktsioon
# siin ei kontrollita tegelase tüüpi (polümorfism)
def lahing(t1, t2):

    print("Lahing:", t1.nimi, "vs", t2.nimi)
    print("----------------------")

    while t1.on_elus() and t2.on_elus():

        t1.ründa(t2)

        if not t2.on_elus():
            break

        t2.ründa(t1)

        print("----------------------")

    if t1.on_elus():
        print("Võitis", t1.nimi)
    else:
        print("Võitis", t2.nimi)


# testimine
s1 = Sõdalane("Soldat", 100)
m1 = Maag("Suurmaag", 80, 50)
v1 = Vibukütt("Vaprake", 90, 10)

lahing(s1, m1)
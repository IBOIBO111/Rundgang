#Klassen
class Mitarbeiter():
    verbindungen = 0
    def __init__(self,_name):
        self.myName = _name
    def anmelden(self):
        Mitarbeiter.verbindungen +=1
        print("Anmeldung erfolgreich")
    def abmelden(self, _vorzeitig):
        if _vorzeitig:
            print("Muss früher weg!")

    @classmethod
    def AnzahlMitarbeiter(cls):
        print("%d angemeldet" %cls.verbindungen)


    #statische Methode
    @staticmethod
    def KlassenInfo():
        print("Diese Klasse sammelt Mitarbeiter....")


    #setter
    def set_age(self,_age):
        print("setter")
        self.myAge = _age

    #getter
    def get_age(self):
        print("getter")
        return self.myAge

    @property
    def alter(self):
        print("getter")
        return self.__Age

    @alter.setter
    def alter(self, _alter):
        print("setter")
        self.__Age = _alter

    Age = property(get_age,set_age)

Teilnehmer = Mitarbeiter("Bruce")
print(Teilnehmer.myName)

Teilnehmer.anmelden()
Teilnehmer.AnzahlMitarbeiter()
Teilnehmer.abmelden(True)

Teilnehmer.Age = 38
alter = Teilnehmer.Age
print(alter)

Teilnehmer.alter = 44
alter = Teilnehmer.alter
print((alter))

#statische Methode
Mitarbeiter.KlassenInfo()



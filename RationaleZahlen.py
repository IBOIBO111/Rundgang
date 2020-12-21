

class Bruchzahl():
    def __init__(self,_ganz=0, _zaehler=0,_nenner=1):
        if(_nenner == 0): raise Exception("Nenner darf nicht null sein!")
        self.ganz = int(_ganz)
        self.zaehler = int(_zaehler)
        self.nenner = int(_nenner)
        self.Nachkommatoleranz = 10
        self.condense()

    def condense(self):
        divTable = (7,5,3,2)
        while(self.zaehler >= self.nenner):
            self.ganz = self.ganz+1
            self.zaehler = self.zaehler-self.nenner

        for div in divTable:
            while(self.zaehler % div == 0) and (self.nenner % div == 0):
                self.zaehler = int(self.zaehler / div)
                self.nenner = int(self.nenner/div)

    def convertDouble(self,_Zahl):
        #Ganzzahl
        test = float(_Zahl)
        ganz = int(test)
        rest = round(float(_Zahl)- float(ganz),self.Nachkommatoleranz);
        partials = [ganz]
        while rest != 0:
            rest = rest * 10
            ganz = int(rest)
            partials.append(ganz)
            rest = round(rest - ganz,self.Nachkommatoleranz)
        Nenner = 10 ** (len(partials) - 1)
        Zaehler = 0
        for i in range(0,len(partials)):
            Zaehler = Zaehler + partials[i]*10**(len(partials) -1- i)


        tnew = Bruchzahl(0,Zaehler,Nenner)
        tnew.condense()
        return tnew

    def Add(self, _other):
        self.zaehler = self.zaehler + _other.zaehler
        self.nenner = self.nenner + _other.nenner
        self.condense()

    def Subst(self,_other):
        self.zaehler = self.zaehler + _other.zaehler
        self.nenner = self.nenner + _other.nenner
        self.condense()

    def giveBreak(self):
        tbreak = ""
        if(self.ganz > 0):
            tbreak = tbreak + str(self.ganz)
        if(self.zaehler > 0):
            tbreak = tbreak + " "+str(self.zaehler)+"/"+str(self.nenner)
        return tbreak


while True:
    Gleit = input("Geben sie eine Dezimalzahl an: ")
    Bruch1 = Bruchzahl(0,0,1)
    Bruch2 = Bruch1.convertDouble(Gleit)
    print(Bruch2.giveBreak())



while True:
    Zahler = input("Geben sie den Zähler des Bruchs an: ")
    Nenner = input("Geben sie den Nenner des Bruchs an:" )
    Bruch = Bruchzahl(0,Zahler,Nenner)
    print(Bruch.giveBreak())










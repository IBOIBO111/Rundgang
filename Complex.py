import math
class Complex():
    def __init__(self,_real,_complex):
        self.__real = float(_real)
        self.__complex = float(_complex)

    def getReal(self):
        return self.__real
    def getComplex(self):
        return self.__complex
    def getBetrag(self):
        return math.sqrt(self.__real**2+self.__complex**2)
    def ComplexString(self):
        return "{}+{}i".format(self.__real,self.__complex)

    def Add(self, _compl):
        r = self.__real + _compl.getReal()
        i = self.__complex + _compl.getComplex()
        return Complex(r,i)


def askForComplex():
    rreal = input("Zahl 1: %d real:" % zaehler)
    if rreal == "q":
        goon = False
        return False
    ccomplex = input("Zahl 1: %d complex:" % zaehler)
    if ccomplex == "q":
        goon = False
        return False
    return Complex(rreal,ccomplex)


print("Programm zum addieren von komplexen Zahlen")
print("Abbruch mit 'q'")
goon = True
zaehler = 1
CompZahl = Complex(0,0)
while goon:
    print("First complex:")
    comp1 = askForComplex()
    if type(comp1) == bool:
        break

    print("Second complex:")
    comp2 = askForComplex()
    if type(comp2) == bool:
        break
    '''CompZahl = AddComplex(CompZahl,Complex(float(rreal),float(ccomplex)))'''
    CompZahl = comp1.Add(comp2)
    zaehler += 1
    print("Resultierende Komplexe Zahl ist [{}]".format(CompZahl.ComplexString()))
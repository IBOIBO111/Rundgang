print("Hallo Welt")
Name = "Ingoli Bolm"
print(Name)

#das ist ein kommentar
Name = "Joe"
pi = 3.141

#Datentypen
#Itneger Werte
a = 5
#negative Zahlen
b = -10
#Float
j = 6.8 #test

k = a * j * 10
print(k)

#bool
istVerbunden = True

#binäre Zahlen
binaereZwei = 0b10
print(binaereZwei)

#hexadezimal
hexa10 = 0xA
print(hexa10)

#Typumwandlung
a = True
intA = int(a)

PreisInEuro = 19.99
PreisIntInEuro = int(PreisInEuro)
print(PreisIntInEuro)

Alter = "39"
AlterInDreiJahren = int(Alter) + 3
print(AlterInDreiJahren)

PreisString = "19.99"
PreisIntInEuro = float(PreisString)
print(PreisIntInEuro)

#Kommentare sehen so aus

"""
Das ist ein Lager Kommentar
"""

#%s - String
name = "Ingo"
print("Hallo, %s. Wie geht es dir?" %name)

#%d - Dezimal
age = 34
print("Du bist %d Jahre alt" %age)

#%f float
wert = 1.25634287
print("du hast %.2f Meter erreicht" %wert)

## Neue Formatierung
output = "Du bist {} Jahre alt".format(age)
print(output)

out2 = "{1}, Du hast {0:.2f}m erreicht".format(wert,name)
print(out2)

# Inputs
userInput = input("Welches Tor?")
if userInput =="Tor1":
    print("Gewonnen!")
else:
    print("Verloren...")

#lokal und global
#globale
wetter = "Sonne"

def regen():
    wetter = "Regen"
    print(wetter)
    print(locals())

regen()
print(wetter)
print(globals())
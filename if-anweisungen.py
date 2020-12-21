istVollJaehrig = False

if istVollJaehrig:
    print("Du bis 18 Jahre alt!")
else:
    print("Du bist noch nicht über 18 Jahre alt")


#FSK
alter = 22
groesse = 150
if alter >= 18:
    print("ab 18")
elif alter >= 16:
    print("ab 16")
elif alter >= 12:
    print("ab 12")
else:
    print("Kind")


# migliedschaft
teilnehmer = {"Peter":True, "Karl":False, "Britta":True, "Heidi":True}

if "Peter" in teilnehmer:
    print("Peter gefunden")

# logische Operationen
mindestalter = 12
mindestGroesse = 166
if alter >= mindestalter or groesse >= mindestGroesse:
    print("OR: Mitfahrt erlaubt")
else:
    print("OR: Keine Mitfahrt erlaubt")

# und
if alter >= mindestalter and groesse >= mindestGroesse:
    print("AND: Mitfahrt erlaubt")
else:
    print("AND: Keine Mitfahrt erlaubt")

# und nicht
Gewicht = 61 #kg
maxGewicht = 60 #kg
if alter >= mindestalter and not Gewicht >= maxGewicht:
    print("AND NOT: Mitfahrt erlaubt")
else:
    print("AND NOT: Keine Mitfahrt erlaubt")

# Randbedingungen
rest = 8 % 2
if rest:
    print("Ungerade Zahl")
else:
    print("Gerade Zahl")

anmeldungen = {}
if anmeldungen:
    print("Es gibt Anmeldungen")
else:
    print("Es gibt keine Anmeldungen")

# floatwerte
hoehe = 0.0
if hoehe:
    print("Gültiger Wert")
else:
    print("ungültiger Wert")
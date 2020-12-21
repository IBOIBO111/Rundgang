leereListe = []
superhelden =["peter parker", "bruece Wayne", "Tomy Stark"]
lottoZahlen = [3, 4, 8, 22, 44]

#Liste
auchLeer = list()

#lesen (n-1):1. Element
print(lottoZahlen[0])
print(lottoZahlen[-2])
superhelden.append("X man")
print(superhelden)

# update
superhelden[0] = "Super Man"
print(superhelden)

# Löschen
del superhelden[0]
superhelden.remove("Tomy Stark")
print(superhelden)

# Anzahl
print(len(superhelden))

# slice
planeten = ["jupiter", "Mars", "Venus", "Erde", "Uranus"]
subliste = planeten[0:2]
print(subliste)
print(planeten[::-1])

#index
indexPlaneten = planeten.index(("Erde"))
print(planeten)
print(indexPlaneten)


# kombieren
helden2 = ["thor", "hulk"]
alleHelden = superhelden + helden2
print(alleHelden)
alleHelden += ["Peter Parker", "Green Lantern"]
print(alleHelden)


##########################################
# Listen
steuersaetze = (5, 8, 4)

# keine Zusweisung möglich!
# steuersätze[2] = 2

ta, te, tu = steuersaetze
print(tu)

lottoZahlen = [33, 56, 13, 47, 48, 77]
Zahlen = tuple(lottoZahlen)

# werte tauschen mit tuples
x = 5
y = 10
print(x, y)

x, y = y, x
print(x, y)





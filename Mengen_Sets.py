mengeA = {1, 3, 5, 7}
mengeB = {2, 4, 5, 9}

#hinzufügen
mengeA.add(10)
mengeB.add(12)
print(mengeA)
print(mengeB)

mengeA.add(1)
mengeA.add(2)
print(mengeA)

mengeA.remove(10)
print(mengeA)

# Abfrage
is7in = 7 in mengeA
print(is7in)

# vereinigungsmenge
vereinigt = mengeA.union(mengeB)
print(vereinigt)

#Schnittmenge
schnitt = mengeA.intersection(mengeB)
print(schnitt)

# differenz
diff = mengeA.difference(mengeB)
print(diff)


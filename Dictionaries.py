empty = {}
alter = {"Legolas": 36, "Frodo": 35, "Aragorn": 99}
print(alter)

#key, value
gefaehrte = "Frodo"
print(alter[gefaehrte])

wert = alter.get(gefaehrte, "nicht gefunden")
print(wert)

gefaehrte = "Sam"
wert = alter.get(gefaehrte, "nicht gefunden")
print(wert)

# update
alter["Frodo"] = 25
print(alter)

#hinzufügen
alter["Yoda"] = 400
print(alter)

#alle löschen
farben = {"weiss":"#ffffff", "schwarz":"#000000"}
print(farben)

farben.clear()
print(farben)

#vorhanden
isFrodo = "Frodo" in alter
print(isFrodo)

# alle keys
namen = alter.keys()
print(namen)


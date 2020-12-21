namen = ["Peter", "Tony" , "Bruece"]

for name in namen:
    print(name)

namen = {"Peter":"Parker","Bruece":"Wayne","Tony":"Stark"}
for name in namen.keys():
    print("Nachname ist %s, Vorname ist %s" %(namen[name],name))

for (vorname, nachname) in namen.items():
    print("%s, %s %s" %(nachname,vorname,nachname))

'''Zählt von 1 bis 20!'''
for i in range(1,21):
    print(i)
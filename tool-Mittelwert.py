werte = list()
count = 0
Mittelwert = 0.0
Summevon = 0

while True:
    wert = input("Wert in grad celsius: ")
    if(wert == "q"):
        break
    werte.append(float(wert))
    Summevon += float(wert)
    count += 1

Mittelwert = 0.0
for value in werte:
    Mittelwert += float(value/len(werte))


print("der Mittelwert ist [%.3f]" %(float(Summevon/count)))
print("der Mittelwert ist [%.3f]" %(Mittelwert))
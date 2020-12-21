
# ACHTUNG Speicher!!
fileInput = open("notizen.txt","rt")
notiz = fileInput.read()
fileInput.close()
print("string num: {}".format(len(notiz)))
print(notiz)

fileInput = open("notizen.txt","rt")
bytes = 2
while True:
    auszug = fileInput.read(bytes)
    print(auszug,end='')
    if len(auszug) < bytes:
        break
fileInput.close()

#readline
fileInput = open("notizen.txt","rt")

while auszug == fileInput.readline():
    print(auszug,end='')
fileInput.close()


#Asu CSV Format lesen
import csv
with open("Produktliste.txt","rt") as Liste:
    header = Liste.readline()
    fields = header.split(",")
    RListe = csv.DictReader(Liste,fields)
    Produkte = [zeile for zeile in RListe]
print(Produkte)
'''Beispileaufgabe aus dem Buch Python fuer Ingenieure und Naturwissenschaftler
Aufgabe 3.10.9
'''
from In_Output import *
from TurtleClass import turtlePrint


ResData = "/home/ibo/EigeneUbuntu/PythonProjects/buch_python_fuer_ingenieure/Daten zum Buch Python fuer Ingenieure 26.8.2019/Loesung der Aufgaben Woyand Python 3.te Auflage/Python_Woyand_Kap3/Ergebnisse2.txt"
tread = ReadFile(ResData)

tlinesSplit = tread.read("\t","*",4)

maxVal = float(tlinesSplit[0][3])
minVal = float(tlinesSplit[0][3])
for il in tlinesSplit:
    maxVal = max(maxVal,float(il[3]))
    minVal = min(minVal,float(il[3]))

Legende = {0.2:"blue",0.4:"green",0.6:"yellow",0.8:"orange",1.0:"red"}
Screen = turtlePrint()

for ilineArray in tlinesSplit:
    ix = float(ilineArray[0])
    iy = float(ilineArray[1])
    iz = float(ilineArray[2])
    ival = float(ilineArray[3])

    legval = ival/(maxVal-minVal)
    icolor = "blue"
    for ilim in Legende.keys():
        if legval < ilim:
            icolor = Legende[ilim]
            break
    Screen.zeichneDot(iy,iz,icolor,15)

test = input("Das wars")




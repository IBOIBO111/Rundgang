#!/home/ibo/EigeneUbuntu/PythonProjects/CodeCutter/venv/lib/python3.6/site-packages
import pandas as pd
import csv

def read_html(filedir,OutDir):
    # Data about Cricket World
    cupURL = "https://en.wikipedia.org/wiki/Cricket_World_Cup"
    # Panda DataFrame

    #Tabelle aus der HTML Seite einlesen
    tables = pd.read_html(filedir)
    print("There are : ",len(tables)," tables")
    print("Take look at table 0")
    #print(tables[0])

    #Tabelle nach allen Gruppen durchsuchen
    iGroup = tables[0].loc[0,'Name']

    tGroup = [iGroup]
    numRows = len(tables[0])
    emptyRowsToDelete = []
    newname = False
    allGroups = [iGroup]
    for index in range(1,numRows):
        if(isinstance(tables[0].loc[index,'Name'],float) ):
            emptyRowsToDelete.append(index)
            newname = True
            continue
        if(newname):
            iGroup = tables[0].loc[index,'Name']
            allGroups.append(iGroup)
            newname = False
        tGroup.append(iGroup)

    #Nullzeilen Löschen
    tables[0] = tables[0].drop(emptyRowsToDelete)

    #Namenzeilen Bereinigen
    tNames = allGroups
    tNames.append('Bestellsumme')
    for iName in tNames:
        cols = tables[0].columns
        cols = cols.drop('Name')
        for iCol in cols:
            tables[0].loc[tables[0]['Name'] == iName,iCol]=''

    #Tabelle um eine select Spalte erweitern
    tables[0]['Bestellgruppe'] = tGroup

    #umrechnen der Einheiten
    tEinheiten = tables[0]['Einheit']
    for index in tEinheiten.index:
        tEinheiten[index] = tEinheiten[index].replace(' ','')
        tEinheiten[index] = tEinheiten[index].replace(',', '.')
        if 'kg' in tEinheiten[index]:
            tEinheiten[index] = tEinheiten[index].replace('kg','')
        elif 'g' in tEinheiten[index]:
            tEinheiten[index] = tEinheiten[index].replace('g','')
            tEinheiten[index] = str(round(float(tEinheiten[index])/1000.0,2))
        elif 'ml' in tEinheiten[index]:
            tEinheiten[index] = tEinheiten[index].replace('ml','')
            tEinheiten[index] = str(round(float(tEinheiten[index])/1000.0,2))
        elif 'l' in tEinheiten[index]:
            tEinheiten[index] = tEinheiten[index].replace('l','')
        elif 'St' in tEinheiten[index]:
            tEinheiten[index] = tEinheiten[index].replace('St', '')

    #Table nach Lagern Gruppieren
    LagerBolm = ['Bolm','WG Rulle','Valentin']
    LagerBolmDict = {}
    for iLager in LagerBolm:
        LagerBolmDict[iLager] = tables[0].loc[tables[0]['Bestellgruppe'] == iLager]
    #BolmList = tables[0].loc[tables[0]['Bestellgruppe'] == 'Bolm']

    LagerWenner = list(set(allGroups) - set(LagerBolm)) # ist der Rest
    LagerWennerDict = {}
    for iLager in LagerWenner:
        LagerWennerDict[iLager] = tables[0].loc[tables[0]['Bestellgruppe'] == iLager]
    #WennerList.drop(Wennerlist['Bestellgruppe'] == LagerBolm)

    #Lagerlisten in gemeinsames Dict
    LagerListen = {'Bolm_Lager':LagerBolmDict, 'Wenner_Lager':LagerWennerDict}

    #Nach Produkten Sortieren und Summieren:
    for lager in LagerListen.keys():
        LagerProducts = {}
        for iGroup in LagerListen[lager]:
            iGroupDict = LagerListen[lager][iGroup]
            #Produktliste der Bestllgruppe
            iProdList = iGroupDict['Name']
            #erste und letzte raus
            for index in iProdList.index:
                iprod = iGroupDict['Name'][index]
                if iprod == iGroup or iprod=='Bestellsumme':
                    continue
                if not iprod in LagerProducts:
                    LagerProducts[iprod] = float(iGroupDict['Einheit'][index])
                else:
                    LagerProducts[iprod] += float(iGroupDict['Einheit'][index])
        # Lagerliste in dict ablegen
        LagerListen[lager] = LagerProducts

    #Lagerliste auswerten

    for lager in LagerListen.keys():
        LagerListe = LagerListen[lager]
        fileOut = OutDir + lager + '.csv'
        with open (fileOut, mode='w') as LagerListeDoc:
            WriteList = csv.writer(LagerListeDoc, delimiter = ',', quoting=csv.QUOTE_MINIMAL)
            for iprod in LagerListe:
                WriteList.writerow([iprod,str(LagerListe[iprod])])




file = "/home/ibo/EigeneUbuntu/PythonProjects/FoodcoopScript/Foodsoft - Bestellung Horst Bode Import-Export GmbH.html"
out = "/home/ibo/EigeneUbuntu/PythonProjects/FoodcoopScript/"
read_html(file,out)
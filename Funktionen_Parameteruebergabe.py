def feierabend():
    pass

feierabend()

#Rückgabewert
def getAlter():
    return 21

print(getAlter())

# Parameter
def addieren(_x,_y):
    summe = _x+_y
    return summe

print(addieren(5,5))

# parameter
def connect(_userName,_passwd):
    print("User [%s] is connected" %_userName)

# positionsparameter
connect("Admin","!372&?fgER")

#keyword parameter
connect(_passwd="!372&?fgER",_userName="Admin")

#default parameter
def wurzelZiehen(_wert,_expon=2):
    return _wert**(1/_expon)
print(wurzelZiehen(8,3))
print(wurzelZiehen(8))

#variadische Funktion, dynamische...
def summieren(*args):
    sum = 0
    for nummer in args:
        sum += nummer
    return sum

print(summieren(1,2,3,4))
print(summieren(20,33))

#Keyword parameter
def safePerson(**keywords):
    print(keywords)

safePerson(name = "Peter", age = 18, name2 = "Bruce")

# None
def deinName():
    print("Jan")

result = deinName()
print(result)

#
if result:
    print(result)
else:
    print("Not defined")

#docstring
def multplizieren(_x,_y):
    '''
    ergibt das Ergebnis der Multiplikation
    zweier Zahlen zurück
    '''
    return _x*_y

print(multplizieren(2,2))


#Funktionen als Datentypen
def rechnen(matheFunktion,_x,_y):
    return matheFunktion(_x,_y)

print(rechnen(addieren,9,9))
print(rechnen(multplizieren(9,9)))
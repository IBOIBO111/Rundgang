#herkömmmlich
nummern = []

for nummer in range(1,6):
    nummern.append((nummer))
print(nummern)

#
nummern = list(range(1,6))
print(nummern)

# neu: comprehensions
meineZahlen = range(1,20)
nummern = [nummer**3 for nummer in meineZahlen]
print(nummern)

# neu: comprehensions mit if
meineZahlen = range(1,20)
nummern = [nummer**3 for nummer in meineZahlen if nummer%2]
print(nummern)

# neu: comprehensions verschachtelte Schleifen
zeilen=[1,2,3,4]
spalten=['a','b','c','d']
"""
for zeile in zeilen:
    for spalte in spalten:
        print(zeile,spalte)
"""
zellen = [(zeile,spalte) for zeile in zeilen for spalte in spalten]
for zelle in zellen:
    print(zelle)

#Dictionary Comprehension
meinText='''
Lorem ipsum dolor sit amet, consetetur 
sadipscing elitr, sed diam nonumy eirmod 
tempor invidunt ut labore et dolore magna aliquyam 
erat, sed diam voluptua. At vero eos et accusam 
et justo duo dolores et ea rebum. Stet clita kasd 
gubergren, no sea takimata sanctus est Lorem ipsum 
dolor sit amet. Lorem ipsum dolor sit amet, consetetur 
sadipscing elitr, sed diam nonumy eirmod tempor invidunt 
ut labore et dolore magna aliquyam erat, sed diam voluptua. 
At vero eos et accusam et justo duo dolores et ea rebum. 
Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet.
'''

buchstaben = set(meinText)
print(buchstaben)

txtStat = {zeichen:meinText.count(zeichen) for zeichen in buchstaben}
print(txtStat)

otherCharts = {char.upper() for char in meinText if char not in 'aeiou'}
print(otherCharts)


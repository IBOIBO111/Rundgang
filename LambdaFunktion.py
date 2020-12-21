preise =[2,5,12,44,56]

def getVK(_preis):
    '''
    Verkaufspreis:
     * 40% Marge
     * 2Euro Vesand
    '''
    return _preis * 1.4 + 2

def preisListing(_preise,func):
    return [func(ek) for ek in _preise]

Listeks = preisListing(preise,getVK)

for eks in Listeks:
    print(eks)

# Alternativ Lambdafunktionen
Listeks = preisListing(preise, lambda ek: ek*1.4+2)
for eks in Listeks:
    print(eks)
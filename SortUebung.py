

def sortThis(_liste):
    numofElem = len(_liste)
    for ielem in range(0,numofElem-1):
        itok = _liste[ielem]
        for jelem in range(ielem+1,numofElem):
            jtok = _liste[jelem]
            if(jtok <itok):
                _liste[ielem] = jtok
                _liste[jelem] = itok
                itok = _liste[ielem]
                jtok = _liste[jelem]
    return _liste

zahlen = [45,23,12.5,2,119.23,44]
sorted = sortThis(zahlen)

print(zahlen)

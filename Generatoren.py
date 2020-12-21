#python 2:
longRange = range(1,10000000)

'''
for k in longRange:
    if k % 1000000==0:
        print(k)
'''

#eigene Range Funktion
def myRange(_start,_stop):
    x = _start
    while x<=_stop:
        yield x
        x += 1

anotherRange = myRange(1,10000000)

for k in anotherRange:
    if k % 1000000==0:
        print(k)


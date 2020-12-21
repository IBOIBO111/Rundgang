class Label():
    def __init__(self, _text):
        self.__text = _text

    def __eq__(self, other):
        return self.__text == other

    def __ne__(self, other):
        return self.__text != other


Label1 = Label("Hallo")
Label2 = Label("Welt")
Label3 = Label("Hallo")

if Label1 == Label3:
    print("sind gleich")
else:
    print("sind nicht gleich")

if Label1 != Label2:
    print("sind nicht gleich die beiden")


class Lottoschein():
    def __init__(self,Zahlen):
        self.__zahlen = Zahlen

    def __len__(self):
        return len(self.__zahlen)


zahlen = [2,4,49,48,47,46]
Schein = Lottoschein(zahlen)
print(len(Schein))
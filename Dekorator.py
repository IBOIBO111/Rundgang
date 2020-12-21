def logDecorator(function):
    def logger(*args):
        print("Funktion: %s" % function.__name__)
        print("Parameter:", args)

        ergebnis = function(*args)
        print("Ergebnis:" + str(ergebnis))
        return ergebnis
    return logger

def quadLogDecoator(function):
    def quadrat(*args):
        ergebnis = function(*args)
        return ergebnis ** 2
    return quadrat

@logDecorator
@quadLogDecoator
def Addieren(_x , _y):
    return _x+_y

#logAddierer = logDecorator(Addieren)
summe = Addieren(10,5)
print(summe)


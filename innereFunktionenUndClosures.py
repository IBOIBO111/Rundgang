def aussen(_x):
    def innen(_y):
        print(_y)

    innen(_x)


aussen(3)


def download(_url):
    def errormsg(_msg):
        print("###", _msg)

    # erfolg Download:
    # ...
    # Misserfolg Download:
    errormsg("Timeout")


download("www.beispiel.de")


# Closure
def hallo(_name):
    def Grußfon():
        return "Hallo, %s" % _name

    Gruß = Grußfon
    #return " %s, wie geht es dir?" % Gruß
    return Gruß
halloFunktion = hallo("Bruce")
print(halloFunktion())


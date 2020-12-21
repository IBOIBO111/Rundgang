class vektor():
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    @property
    def xval(self):
        return self.__x
    @property
    def yval(self):
        return self.__y

    '''vec: vektor = property(get_v,set_v)'''

    def add(self,other):
        x = self.__x + other.xval
        y = self.__y + other.yval
        return vektor(x,y)


def fakultaet(_n:int) -> int:
    if float(_n) < 2:
        return 1
    else:
        return _n*fakultaet(_n-1)


def fibonacci(_n:int) -> int:
    if(_n==1):
        return 1
    elif(_n==2):
        return 1
    else:
        return fibonacci(_n-1) + fibonacci(_n-2)

zahl = input("n = ")
print("Fibonacci = "+str(fibonacci(int(zahl))))



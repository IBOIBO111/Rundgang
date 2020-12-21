# Basisklasse / Superklasse / Elternklasse
class DBAdabter():
    def __init__(self, _userName, _passWord):
        self.myUser = _userName
        self.myPassWord = _passWord

    def connect(self):
        print("Verbindung aufgebaut")

# Kindklasse
class MySQLAdapter(DBAdabter):
    def __init__(self, _Name, _pass):
        super().__init__(_Name,_pass)
        self.connect()

    def connect(self):
        print("mySQL Verbindung aufgebaut")


mySQL = MySQLAdapter("Bruce","dfetgsr762TGf")
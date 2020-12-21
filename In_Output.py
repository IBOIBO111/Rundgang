import re
import os

class ReadFile():
    def __init__(self,_textfile):
        self.myTextfile = _textfile
        if not(os.path.isfile(self.myTextfile)):
            raise Exception("File %s not found!"%(self.myTextfile))

    def read(self,_seperatorString, _commentString, _startAtLine) -> list():
        rd = open(self.myTextfile,"rt")
        tList = list()

        iline = ""
        token = 0
        while True:
            iline = rd.readline()
            if len(iline) < 1:
                break

            token = token +1
            if(token < _startAtLine):
                continue

            iline = iline.strip()
            pattern = "("+_commentString+")+"
            pattern = " +"
            icomment = iline.split(_commentString)
            itxt = icomment[0]
            iLineSplit = re.split(_seperatorString+"+",itxt)
            tList.append(iLineSplit)

        rd.close()
        return tList

class WriteFile():
    def __init__(self,_textfile,_overwrite = False):
        self.myTextfile = _textfile
        self.myOverwrite = _overwrite
        if self.myTextfile.is_file() and _overwrite:
            os.remove(self.myTextfile)

        def writeLine(_line):
            wt = open(self.myTextfile,"wt")
            wt.writelines(list(_line))
            wt.close()

        def writeLines(_lines):
            wt = open(self.myTextfile,"wt")
            wt.writelines(_lines)
            wt.close()






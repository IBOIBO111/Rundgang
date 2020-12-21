def Rechnen(_operat, _z1, _z2):
    try:
        if _operat == "+":
            return float(_z1) + float(_z2)
        elif _operat == "-":
            return float(_z1) - float(_z2)
        elif _operat == "*":
            return float(_z1) * float(_z2)
        elif _operat == "/":
            return float(_z1) / float(_z2)
        else:
            raise Exception("Operator[%s] not valid!" %_operat)
    except Exception as error:
        print(error)


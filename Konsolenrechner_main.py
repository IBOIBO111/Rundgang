import Konsolenrechner_module as mod

goon = True
while goon:
    operator = input("Operator: +, -, *, /, q")

    try:
        if operator == "+" or operator == "-" or operator=="*" or operator == "/":
            ersteZahl = input("Zahl 1:")
            zweiteZahl = input("Zahl 2:")
            res = mod.Rechnen(operator,ersteZahl,zweiteZahl)
            print("Ergebnis ist %.2f" % res)
        elif operator == "q":
            goon = False
            break
        else:
            raise Exception("Not a valid Operator chosen!")


    except Exception as error:
        print(error)

















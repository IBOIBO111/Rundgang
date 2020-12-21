from turtle import *

class turtlePrint():
    def __init__(self,_minwert = -20,_maxwert = 220):
        setworldcoordinates(_minwert,_minwert,_maxwert,_maxwert)
        speed(0)
        hideturtle()

    def zeichneDot(self,_xa,_ya,_color="red",_size=3):
        penup()
        goto(int(_xa),int(_ya))
        dot(_size,_color)

    def zeichne_Rechteck(self,_xa,_ya,_breite,_hoehe):
        pensize(4)
        penup()
        goto(int(_xa),int(_ya))
        pendown()
        for i in range(2):
            forward(int(_breite))
            left(90)
            forward(int(_hoehe))
            left(90)
        return


    def zeichne_Dreieck(self,_xa,_ya,_kantenlaenge):
        pensize(4)
        penup()
        goto(int(_xa),int(_ya))
        pendown()
        for i in range(3):
            forward(int(_kantenlaenge))
            left(120)
        return

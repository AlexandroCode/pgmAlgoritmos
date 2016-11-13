from MainCode import *

p1 = instrucciones([-3, -6, -2, 8], [], [0, 0, 0, 1], 0, 0, 1) #constructor

while (len(p1.listaEntrada) != 0 or p1.monito > 0):

    if p1.paso == 1:
        p1.entrada()

    if p1.paso == 2:
        p1.copiarA(0)

    if p1.paso == 3:
        p1.entrada()

    if p1.paso == 4:
        p1.irNeg(9)

    if p1.paso == 5:
        p1.copiarDe(0)

    if p1.paso == 6:
        p1.irNeg(12)

    if p1.paso == 7:
        p1.copiarDe(2)

    if p1.paso == 8:
        p1.irA(13)

    if p1.paso == 9:
        p1.copiarDe(0)

    if p1.paso == 10:
        p1.irNeg(7)

    if p1.paso == 11:
        p1.irA(7)

    if p1.paso == 12:
        p1.copiarDe(3)

    if p1.paso == 13:
        p1.salida()

    if p1.paso == 14:
        p1.irA(1)
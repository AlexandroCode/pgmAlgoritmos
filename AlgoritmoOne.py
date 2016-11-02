
from MainCode import *

p1 = instrucciones([-3, -6, -2, 8], [], [0, 0, 0, 1], 0, 0, 1) #constructor

while (len(p1.listaEntrada) != 0):

    if  p1.paso == 1:
        p1.entrada()

    if  p1.paso == 2:
        p1.copiarA(0)

    if  p1.paso == 3:
        p1.irNeg(5)

    if  p1.paso == 4:
        p1.irA(7)

    if  p1.paso == 5:
        p1.restar(0)

    if  p1.paso == 6:
        p1.restar(0)

    if  p1.paso == 7:
        p1.salida()

    if  p1.paso == 8:
        p1.irA(1)

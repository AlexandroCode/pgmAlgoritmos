import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QLabel, QLineEdit, QAbstractItemView, QPushButton
from PyQt5 import uic
#from PyQt5.QtCore import Qt, QMimeData
from PyQt5 import QtGui
from MainCode import *
'''
class DialogoInicio(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.resize(350, 200)
        self.setWindowTitle("Inicio del juego")
        self.etiqueta1 = QLabel(self)
        self.etiqueta2 = QLabel(self)
        self.texto1 = QLineEdit(self)
        self.btnAceptar1 = QPushButton(self)
        self.btnCancelar1 =QPushButton(self)
'''


class mainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        uic.loadUi("interfaz.ui", self)
        self.setWindowTitle("Principal")
        self.dialogo = Dialogo()
        self.Inicio = Dialogo()
        self.listInstrucciones.setDragDropMode(QAbstractItemView.InternalMove)
        #self.Iniciar()

        self.btnEntrada.clicked.connect(self.addEntrada)
        self.btnSalida.clicked.connect(self.addSalida)
        self.btnIra.clicked.connect(self.addIra)
        self.btnIrnegativo.clicked.connect(self.addIrnegativo)
        self.btnIrcero.clicked.connect(self.addIrcero)
        self.btnCopiara.clicked.connect(self.addCopiara)
        self.btnCopiarde.clicked.connect(self.addCopiarde)
        self.btnMasMas.clicked.connect(self.addMasMas)
        self.btnMenosMenos.clicked.connect(self.addMenosMenos)
        self.btnSumar.clicked.connect(self.addSumar)
        self.btnRestar.clicked.connect(self.addRestar)
        self.btnborrar.clicked.connect(self.removePaso)

    def Iniciar(self):
        self.setWindowTitle("Inicio del juego")
        self.Inicio.etiqueta.setText("Lista de Entrada Aleatoria")
        #self.Inicio.etiqueta2.setText("¿Lista de Entrada Personalizada?")
        self.Inicio.etiqueta.move(10, 15)
        #self.Inicio.etiqueta2.move(100, 15)
        self.Inicio.btnAceptar.move(30, 65)
        self.Inicio.btnAceptar.setText("Aceptar")
        self.Inicio.btnCancelar.move(120, 65)
        self.Inicio.btnCancelar.setText("Cancelar")
        self.Inicio.btnAceptar.clicked.connect(self.aceptarDialogo)
        self.Inicio.btnCancelar.clicked.connect(self.cancelarDialogo)
        self.dialogo.exec_()


    def removePaso(self):
        for item in self.listInstrucciones.selectedItems():
            self.listInstrucciones.takeItem(self.listInstrucciones.row(item))

    def addEntrada(self):
        self.listInstrucciones.addItem("Entrada")

    def addSalida(self):
        self.listInstrucciones.addItem("Salida")

    def addMasMas(self):
        self.listInstrucciones.addItem("+ + + ( )")

    def addMenosMenos(self):
        self.listInstrucciones.addItem("- - - ( )")

    def addIrnegativo(self):
        self.dialogoIra()
        if self.irPaso != "":
            self.listInstrucciones.addItem("Ir si es Negativo ("+ self.irPaso +")")

    def addIrcero(self):
        self.dialogoIra()
        if self.irPaso != "":
            self.listInstrucciones.addItem("Ir si es cero (" + self.irPaso + ")")

    def addIra(self):
        self.dialogoIra()
        if self.irPaso != "":
            self.listInstrucciones.addItem("Ir a paso (" + self.irPaso + ")")

    def addCopiara(self):
        self.dialogoCopiar()
        if self.irPaso != "":
            self.listInstrucciones.addItem("Copiar a (" + self.irPaso + ")")

    def addCopiarde(self):
        self.dialogoCopiar()
        if self.irPaso != "":
            self.listInstrucciones.addItem("Copiar de (" + self.irPaso + ")")

    def addSumar(self):
        self.dialogoCopiar()
        if self.irPaso != "":
            self.listInstrucciones.addItem("Sumar de (" + self.irPaso + ")")

    def addRestar(self):
        self.dialogoCopiar()
        if self.irPaso != "":
            self.listInstrucciones.addItem("Restar de (" + self.irPaso + ")")

    def dialogoIra(self):
        self.irPaso = ""
        self.dialogo.etiqueta.setText("¿A qué paso quiere ir?")
        self.dialogo.etiqueta.move(50, 15)
        self.dialogo.texto.move(60, 40)
        self.dialogo.texto.clear()
        self.dialogo.btnAceptar.move(30,65)
        self.dialogo.btnAceptar.setText("Aceptar")
        self.dialogo.btnCancelar.move(120, 65)
        self.dialogo.btnCancelar.setText("Cancelar")
        self.dialogo.btnAceptar.clicked.connect(self.aceptarDialogo)
        self.dialogo.btnCancelar.clicked.connect(self.cancelarDialogo)
        self.dialogo.exec_()

    def dialogoCopiar(self):
        self.irPaso = ""
        self.dialogo.etiqueta.setText("¿Seleccione posicion en suelo?")
        self.dialogo.etiqueta.move(25, 15)
        self.dialogo.texto.move(60, 40)
        self.dialogo.texto.clear()
        self.dialogo.btnAceptar.move(30, 65)
        self.dialogo.btnAceptar.setText("Aceptar")
        self.dialogo.btnCancelar.move(120, 65)
        self.dialogo.btnCancelar.setText("Cancelar")
        self.dialogo.btnAceptar.clicked.connect(self.aceptarDialogo)
        self.dialogo.btnCancelar.clicked.connect(self.cancelarDialogo)
        self.dialogo.exec_()

    def aceptarDialogo(self):
        global irPaso
        self.irPaso = self.dialogo.texto.text()
        #self.dialogo.irPaso.setText(irPaso)
        self.dialogo.close()

    def cancelarDialogo(self):
        self.dialogo.close()

class addInstruccion():
    def __init__(self, nameInstruccion):
        self.nameInstruccion = nameInstruccion


class Dialogo(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.resize(250, 100)
        self.setWindowTitle("Parametros")
        self.etiqueta = QLabel(self)
        self.texto = QLineEdit(self)
        self.btnAceptar = QPushButton(self)
        self.btnCancelar =QPushButton(self)


app = QApplication(sys.argv)
ventana = mainWindow()
ventana.show()
app.exec_()
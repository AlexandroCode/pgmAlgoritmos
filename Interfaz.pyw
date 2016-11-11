import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QLabel, QLineEdit
from PyQt5 import uic
#from PyQt5.QtCore import Qt, QMimeData
#from PyQt5.QtGui import QDrag



class mainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        uic.loadUi("interfaz.ui", self)
        self.setWindowTitle("Principal")
        self.dialogo = Dialogo()

        self.btnEntrada.clicked.connect(self.addEntrada)

    def addEntrada(self):
        pass

class addInstruccion():
    def __init__(self, nameInstruccion):
        self.nameInstruccion = nameInstruccion

class Dialogo(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.resize(250, 100)
        self.setWindowTitle("Ventana Dialogo")
        self.etiqueta = QLabel(self)
        self.texto = QLineEdit(self)



app = QApplication(sys.argv)
ventana = mainWindow()
ventana.show()
app.exec_()
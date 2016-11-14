import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import Qt, QMimeData
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from MainCode import *
import random
import subprocess
import os

class DialogoInicio(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi("Inicio.ui", self)

        #self.btnSalir.clicked.connect(self.cancelarInicio)
    '''
    def radio_value(self):
        if self.rbtnAleatoria.isChecked():
            self.btnAdd.disable()
    '''

class DialogoEjecutar(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi("vEjecucion.ui", self)

class mainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        uic.loadUi("interfaz.ui", self)
        self.setWindowTitle("Principal")
        self.dialogo = Dialogo()
        self.Inicio = DialogoInicio()
        self.execute = DialogoEjecutar()
        self.listInstrucciones.setDragDropMode(QAbstractItemView.InternalMove)
        self.btnstart.clicked.connect(self.Iniciar)
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
        self.myrandoms = [random.randrange(-101, 101) for _ in range(10)]
        self.btnEjecutar.clicked.connect(self.getAlgoritmo)
        self.btnCargar.clicked.connect(self.buildInstrucciones)
        self.btnExeShell.clicked.connect(lambda:self.run('solucion.py'))
        self.btnSalir.clicked.connect(self.cerrarMain)
        self.btnGuardar.clicked.connect(self.saveAlgoritmo)

    def cerrarMain(self):
        resp =  QMessageBox.question(self, "Cerrar", "Cerrar aplicacion", QMessageBox.Ok, QMessageBox.Cancel)
        if resp == QMessageBox.Ok:
            self.close()
        else:
            return

    def run(self, path):
        subprocess.call(['pythonw',path])

    def Iniciar(self):
        self.Inicio.open()
        #uic.loadUi("Interfaz.ui", self)
        self.Inicio.btnSalir.clicked.connect(self.cancelarInicio)
        self.Inicio.rbtnAleatoria.clicked.connect(self.radioValor)
        self.Inicio.rbtnllenar.clicked.connect(self.radioValor)
        self.Inicio.btnContinuar.clicked.connect(self.aPrincipal)
        for numero in self.myrandoms:
            self.Inicio.listNumInicio.addItem(str(numero))

    def radioValor(self):
        self.Inicio.btnContinuar.setFocus()
        if self.Inicio.rbtnllenar.isChecked():
            self.Inicio.btnAdd.setEnabled(True)
            self.Inicio.listNumInicio.clear()
            self.Inicio.btnAdd.setFocus()
        else:
            self.Inicio.btnAdd.setEnabled(False)
            self.Inicio.btnContinuar.setFocus()
            for numero in self.myrandoms:
                self.Inicio.listNumInicio.addItem(str(numero))

    def cancelarInicio(self):
        self.Inicio.listNumInicio.clear()
        self.Inicio.close()
        instrucciones.listaEntrada = []
        print(instrucciones.listaEntrada)

    def ventanaEjecutar(self):
        self.execute.open()
        self.execute.setWindowTitle("Ejecutando Algoritmo")
        self.buildInstruccionesExe()
        self.addNumEntradaExe()
        self.execute.btnCancelar.clicked.connect(self.cancelarExe)
        self.execute.btnIniciar.clicked.connect(self.ejecutaAlgoritmo)
        pixmap = QPixmap('user.png')
        self.execute.lblmonito.setPixmap(pixmap)
        self.execute.lblmonito.show()

    def ejecutaAlgoritmo(self):
        #print (self.execute.listPasosExe.currentRow(0))
        #print(self.execute.listPasosExe.currentRow())
        pass

    def cancelarExe(self):
        self.execute.listEntrada.clear()
        self.execute.listPasosExe.clear()
        self.execute.close()

    def aPrincipal(self):
        instrucciones.listaEntrada = self.myrandoms
        self.Inicio.listNumInicio.clear()
        self.Inicio.close()
        print (instrucciones.listaEntrada)

    def removePaso(self):
        resp = QMessageBox.warning(self, "Eliminar", "Eliminar Instruccion", QMessageBox.Abort, QMessageBox.Apply)
        if resp == QMessageBox.Apply:
            for item in self.listInstrucciones.selectedItems():
                self.listInstrucciones.takeItem(self.listInstrucciones.row(item))
        else:
            return


    def addEntrada(self):
        #for index in range(self.listInstrucciones.count()):
            #self.pos = index
        #itm = QListWidgetItem(str(self.listInstrucciones.count()))
        itm = QListWidgetItem("entrada()")
        itm.setIcon(QIcon(r"user.png"))
        self.listInstrucciones.addItem(itm)
        #self.listInstrucciones.addItem("entrada()")

    def addSalida(self):
        itm = QListWidgetItem("salida()")
        itm.setIcon(QIcon(r"user.png"))
        self.listInstrucciones.addItem(itm)
        #self.listInstrucciones.addItem("salida()")

    def addMasMas(self):
        itm = QListWidgetItem("masmas()")
        itm.setIcon(QIcon(r"user.png"))
        self.listInstrucciones.addItem(itm)
        #self.listInstrucciones.addItem("masmas()")

    def addMenosMenos(self):
        itm = QListWidgetItem("menosmenos()")
        itm.setIcon(QIcon(r"user.png"))
        self.listInstrucciones.addItem(itm)
        #self.listInstrucciones.addItem("menosmenos")

    def addIrnegativo(self):
        self.dialogoIra()
        if self.irPaso != "":
            itm = QListWidgetItem("irNeg("+self.irPaso+")")
            itm.setIcon(QIcon(r"user.png"))
            self.listInstrucciones.addItem(itm)
            #self.listInstrucciones.addItem("irNeg("+ self.irPaso +")")

    def addIrcero(self):
        self.dialogoIra()
        if self.irPaso != "":
            itm = QListWidgetItem("irCero(" + self.irPaso + ")")
            itm.setIcon(QIcon(r"user.png"))
            self.listInstrucciones.addItem(itm)
            #self.listInstrucciones.addItem("irCero(" + self.irPaso + ")")

    def addIra(self):
        self.dialogoIra()
        if self.irPaso != "":
            itm = QListWidgetItem("irA(" + self.irPaso + ")")
            itm.setIcon(QIcon(r"user.png"))
            self.listInstrucciones.addItem(itm)
            #self.listInstrucciones.addItem("irA(" + self.irPaso + ")")

    def addCopiara(self):
        self.dialogoCopiar()
        if self.irPaso != "":
            itm = QListWidgetItem("copiarA(" + self.irPaso + ")")
            itm.setIcon(QIcon(r"user.png"))
            self.listInstrucciones.addItem(itm)
            #self.listInstrucciones.addItem("copiarA(" + self.irPaso + ")")

    def addCopiarde(self):
        self.dialogoCopiar()
        if self.irPaso != "":
            itm = QListWidgetItem("copiarDe(" + self.irPaso + ")")
            itm.setIcon(QIcon(r"user.png"))
            self.listInstrucciones.addItem(itm)
            #self.listInstrucciones.addItem("copiarDe(" + self.irPaso + ")")

    def addSumar(self):
        self.dialogoCopiar()
        if self.irPaso != "":
            itm = QListWidgetItem("sumar(" + self.irPaso + ")")
            itm.setIcon(QIcon(r"user.png"))
            self.listInstrucciones.addItem(itm)
            #self.listInstrucciones.addItem("sumar(" + self.irPaso + ")")

    def addRestar(self):
        self.dialogoCopiar()
        if self.irPaso != "":
            itm = QListWidgetItem("restar(" + self.irPaso + ")")
            itm.setIcon(QIcon(r"user.png"))
            self.listInstrucciones.addItem(itm)
            #self.listInstrucciones.addItem("restar(" + self.irPaso + ")")

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
        self.dialogo.etiqueta.setText("Seleccione posicion en suelo")
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

    def getAlgoritmo(self):
        items = []
        #lst = [i.text() for i in self.listInstrucciones.findItems("", QtCore.Qt.MatchContains)]
        #print (lst)
        # itemsTextList = [str(self.listInstrucciones.item(i).text()) for i in range(self.listInstrucciones.count())]
        # print(itemsTextList)
        instrucciones.listaEntrada = self.myrandoms
        file = open("solucion.py", "w+")
        file.write('from MainCode import * \np1 = instrucciones('+str(instrucciones.listaEntrada)+', [], [0, 0, 0, 1], 0, 0, 0)\n')
        file.write('while ((len(p1.listaEntrada) != 0) or p1.monito > 0):\n')
        for index in range(self.listInstrucciones.count()):
            items.append(self.listInstrucciones.item(index))
            label = [i.text() for i in items]
            instruccion = label[0]
            #print (instruccion)
            contenido = file.read()
            finalArchivo = file.tell()
            file.write('    if p1.paso == '+str(index)+':\n')
            file.write('        p1.'+instruccion+'\n')
            file.seek(finalArchivo)
            items = []
        #os.rename("solucion.txt", "solucion.py")
        file.close()
        #print(index)
        self.ventanaEjecutar()

    def saveAlgoritmo(self):
        resp =  QMessageBox.question(self, "Guardar", "Guardar este algoritmo", QMessageBox.Save, QMessageBox.Discard)
        if resp == QMessageBox.Save:
            instrucciones.listaEntrada = self.myrandoms
            file = open("solucion.py", "w+")
            file.write('from MainCode import * \np1 = instrucciones(' + str(
                instrucciones.listaEntrada) + ', [], [0, 0, 0, 1], 0, 0, 0)\n')
            file.write('while ((len(p1.listaEntrada) != 0) or p1.monito > 0):\n')
            for index in range(self.listInstrucciones.count()):
                items.append(self.listInstrucciones.item(index))
                label = [i.text() for i in items]
                instruccion = label[0]
                contenido = file.read()
                finalArchivo = file.tell()
                file.write('    if p1.paso == ' + str(index) + ':\n')
                file.write('        p1.' + instruccion + '\n')
                file.seek(finalArchivo)
                items = []
            # os.rename("solucion.txt", "solucion.py")
            file.close()
        else:
            return

    def buildInstrucciones(self):
        #os.rename("solucion.py","solucion.txt")
        '''
        dlg = QFileDialog()
        dlg.setFileMode(QFileDialog.AnyFile)
        dlg.setFilter("Text files (*.txt)")
        self.filenames = QStringListModel()
        if dlg.exec_():
            self.filenames = dlg.selectedFiles()
        '''
        self.listInstrucciones.clear()
        with open("solucion.py") as lineas:
            for linea in lineas:
                if "entrada" in linea:
                    self.listInstrucciones.addItem(linea[11:])
                elif "salida" in linea:
                    self.listInstrucciones.addItem(linea[11:])
                elif "masmas" in linea:
                    self.listInstrucciones.addItem(linea[11:])
                elif "menosmenos" in linea:
                    self.listInstrucciones.addItem(linea[11:])
                elif "irNeg" in linea:
                    self.listInstrucciones.addItem(linea[11:])
                elif "irCero" in linea:
                    self.listInstrucciones.addItem(linea[11:])
                elif "irA" in linea:
                    self.listInstrucciones.addItem(linea[11:])
                elif "copiarA" in linea:
                    self.listInstrucciones.addItem(linea[11:])
                elif "copiarDe" in linea:
                    self.listInstrucciones.addItem(linea[11:])
                elif "sumar" in linea:
                    self.listInstrucciones.addItem(linea[11:])
                elif "restar" in linea:
                    self.listInstrucciones.addItem(linea[11:])

    def buildInstruccionesExe(self):
        # os.rename("solucion.py","solucion.txt")

        with open("solucion.py") as lineas:
            for linea in lineas:
                if "entrada" in linea:
                    self.execute.listPasosExe.addItem(linea[11:])
                elif "salida" in linea:
                    self.execute.listPasosExe.addItem(linea[11:])
                elif "masmas" in linea:
                    self.execute.listPasosExe.addItem(linea[11:])
                elif "menosmenos" in linea:
                    self.execute.listPasosExe.addItem(linea[11:])
                elif "irNeg" in linea:
                    self.execute.listPasosExe.addItem(linea[11:])
                elif "irCero" in linea:
                    self.execute.listPasosExe.addItem(linea[11:])
                elif "irA" in linea:
                    self.execute.listPasosExe.addItem(linea[11:])
                elif "copiarA" in linea:
                    self.execute.listPasosExe.addItem(linea[11:])
                elif "copiarDe" in linea:
                    self.execute.listPasosExe.addItem(linea[11:])
                elif "sumar" in linea:
                    self.execute.listPasosExe.addItem(linea[11:])
                elif "restar" in linea:
                    self.execute.listPasosExe.addItem(linea[11:])

    def addNumEntradaExe(self):
        instrucciones.listaEntrada = self.myrandoms
        for items in instrucciones.listaEntrada:
            self.execute.listEntrada.addItem(str(items))
        pass

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
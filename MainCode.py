class instrucciones:
    def __init__(self, listaEntrada, listaSalida, listaSuelo, monito, num, paso):
        self.listaEntrada = listaEntrada
        self.listaSalida = listaSalida
        self.listaSuelo = listaSuelo
        self.monito = monito
        self.num = num
        self.paso = paso
    '''
    def algoritmo(self, listaPasos):
        diccionario = {}
        diccionario[1] = "entrada"
        diccionario[2] = " copiarA"
        diccionario[3] = "ir a"
        diccionario[4] = "Restar"
        diccionario[5] = "ir Negativo"
        self.listaPasos = listaPasos
    '''
    def entrada(self):
        self.monito = self.listaEntrada.pop(0)
        self.paso = self.paso + 1

    def salida (self):
        self.listaSalida.append(self.monito)
        self.monito = 0
        self.paso = self.paso + 1
        print (self.listaSalida)
        #print (self.listaSuelo)

    def copiarA(self, n):
        self.listaSuelo[n] = self.monito
        self.paso = self.paso + 1

    def copiarDe(self, n):
        if n == 0:
            self.monito = self.listaSuelo[0]
        else:
            self.monito = self.listaSuelo[n]
        self.paso = self.paso + 1

    def irA(self, n):
        self.paso = n

    def irNeg(self, n):
        if self.monito < 0:
           self.paso = n
        else:
           self.paso = self.paso + 1

    def irCero(self, n):
        if self.monito == 0:
            self.paso = n
        else:
            self.paso = self.paso + 1

    def restar(self, n):
        #print(self.listaSuelo[n])
        #print(self.monito)
        self.monito = self.monito - (self.listaSuelo[n])
        #print(self.monito)
        self.paso = self.paso + 1

    def sumar(self, n):
        self.monito = self.listaSuelo[n] + self.monito
        self.paso =self.paso + 1

    def menosmenos(self):
        self.monito = self.monito - 1
        self.paso = self.paso + 1
        #print (self.monito)

    def masmas(self):
        self.monito = self.monito + 1
        self.paso = self.paso + 1
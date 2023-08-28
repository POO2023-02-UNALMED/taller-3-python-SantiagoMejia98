from televisores.marca import Marca
from televisores.control import Control

class TV:

    _canal = 1
    _precio = 500
    _volumen = 1
    _numTV = 0

    def __init__(self, marca, estado):
        self._marca = marca
        self._estado = estado
        _numTV += 1

    def setMarca(self, marca):
        self._marca = marca

    def getMarca(self):
        return self._marca
    
    def setCanal(self, canal):
        if(self._estado == True and canal >= 1 and canal <= 120):
            self._canal = canal

    def getCanal(self):
        return self._canal
    
    def setPrecio(self, precio):
        self._precio = precio

    def getPrecio(self):
        return self._precio
    
    def setVolumen(self, volumen):
        if(self._estado ==  True and volumen <= 7 and volumen >= 0):
            self._volumen = volumen
    
    def getVolumen(self):
        return self._volumen
    
    def setControl(self, control):
        self._control = control
    
    def getControl(self):
        return self._control
    
    @classmethod
    def setNumTV(num):
        _numTV = num
    
    @classmethod
    def getNumTV():
        return _numTV
    
    def turnOn(self):
        self._estado = True
    
    def turnOff(self):
        self._estado = False

    def getEstado(self):
        return self._estado
    
    def canalUp(self):
        if(self._estado == True and self._canal < 120):
            self._canal += 1

    def canalDown(self):
        if(self._estado == True and self._canal > 1):
            self._canal -= 1

    def volumenUp(self):
        if(self._estado == True and self._volumen < 7):
            self._volumen += 1
    
    def volumenDown(self):
        if(self._estado == True and self._volumen > 0):
            self._volumen -= 1
     
from televisores.tv import TV
from televisores.marca import Marca

class Control:  
    
    def turnOn(self):
        self._tv.turnOn()
    
    def turnOff(self):
        self._tv.turnOff()

    def canalUp(self):
        self._tv.canalUp()

    def volumenUp(self):
        self._tv.volumenUp()

    def volumenDown(self):
        self._tv.volumenDown()

    def setCanal(self, canal):
        self._tv.setCanal(canal)  

    def setVolumen(self, volumen):
        self._tv.setVolumen(volumen)

    def enlazar(self, tv):
        self._tv = tv
        self._tv.setControl(self)
    
    def setTv(self, tv):
        self._tv = tv

    def getTv(self):
        return self._tv
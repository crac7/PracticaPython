class Automovil:

    def __init__(self, modelo, marca, color):
        self.modelo=modelo
        self.marca=marca
        self.color=color
        self._estado='en_reposo'
        self._motor= Motor(cilindros=4)

    def acelerar(self, tipo='despacio'):
        if tipo == 'rapida':
            self._motor.inyect_gasolina(10)
        else :
            self._motor.inyect_gasolina(3)

        self._estado='en_movimiento'

     def frenar(self)  
        self._estado='en_reposo' 

class Motor:

    def __init__(self, cilindros, tipo='gasolina'):
        self.cilindros=cilindros
        self.tipo= tipo
        self._temperatura=0

    def inyect_gasolina(self, cantidad):
        pass

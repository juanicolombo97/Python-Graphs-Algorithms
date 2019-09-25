class Pila:

    def __init__(self):
        self.datos = []
        self.cantidad = 0

    def esta_vacia(self):
        return self.cantidad == 0

    def ver_tope(self):
        if len(self.datos) == 0:
            return None
        return self.datos[len(self.datos)-1]


    def apilar(self,valor):
        self.datos.append(valor)
        self.cantidad+=1
        return True

    def desapilar_valor(self,valor):
        if len(self.datos) == 0:
            return False
        self.cantidad-=1
        self.datos.remove(valor)
        return valor

    def desapilar(self):
        self.cantidad-=1
        return self.datos.pop()

    def cantidad(self):
        return self.cantidad

    def elementos(self):
        return self.datos

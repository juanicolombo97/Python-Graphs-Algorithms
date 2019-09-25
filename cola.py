class Cola:

    def __init__(self):
        self.cola = []
        self.cantidad = 0

    def cantidad(self):
        return self.cantidad

    def esta_vacia(self):
        return self.cantidad == 0

    def encolar(self,valor):
        self.cantidad+=1
        self.cola.insert(0,valor)
        return True
    def desencolar(self):
        if self.cantidad == 0:
            return None
        self.cantidad-=1
        return self.cola.pop()
    def desencolar_valor(self,valor):
        if self.cantidad == 0:
            return None
        self.cantidad-=1
        return self.cola.remove(valor)

    def elementos(self):
        return self.cola

    def cantidad(self):
        return self.cantidad


    def ver_tope(self):
        if self.cantidad == 0:
            return None
        return self.cola[self.cantidad-1]

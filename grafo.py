import random
class Grafo:

    def __init__(self):
        self.vertices = {}
        self.cantidad = 0

    def pertenece_vertice(self,vertice):
        return vertice in self.vertices


    def agregar_vertice(self,vertice):
        self.vertices[vertice] = []
        self.cantidad+=1;
        return True

    def agregar_arista(self,v_inicio,v_fin):
        if not self.pertenece_vertice(v_inicio):
             self.agregar_vertice(v_inicio)
        if not self.pertenece_vertice(v_fin):
            self.agregar_vertice(v_fin)
        self.vertices[v_inicio].append(v_fin)
        return True


    def adyacentes(self,vertice):
        if self.pertenece_vertice(vertice) == False:
            return None
        return self.vertices[vertice]

    def adyacente_aleatorio(self,vertice):
        if self.pertenece_vertice(vertice) == False:
            return None
        adyacentes = self.vertices[vertice]
        if adyacentes == []:
            return None
        return adyacentes[random.randrange(len(adyacentes))]

    def obtener_vertices(self):
        return self.vertices.keys()

    def lista_adyacencia(self):
        print("[")
        for x in self.vertices:
            print(x,":",self.vertices[x])
        print("]")


    def vertice_aleatorio(self):
        lista = []
        for x in self.obtener_vertices():
            lista.append(x)
        return lista[random.randrange(len(lista)-1)]

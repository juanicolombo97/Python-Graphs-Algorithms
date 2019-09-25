from grafo import *
from pila import *
from cola import *
from biblioteca import *
import sys

def pruebas_grafo_vertices():
    print("Pruebas vertice\n")
    g = Grafo()
    g.agregar_vertice(1)
    g.agregar_vertice(2)
    g.agregar_vertice(3)
    g.agregar_vertice(4)
    print("Me fijo que se inserten correctamente los vertices")
    vertices = g.obtener_vertices()
    for x in vertices:
        print(x)
        ok = g.pertenece_vertice(x)
        print("El vertice",x," pertenece:",ok)
        print("El vertice se obtiene",x)
    print("Pruebo agregar vertice ya agregado")
    vertice_rep = g.agregar_vertice(2)
    print("Vertice repetido: ",vertice_rep)
    print("Si inserto repetiod el largo sigue igual",len(g.obtener_vertices())== 4)
    print("Vertices aleatorios: \n")
    for x in range(100):
        g.agregar_vertice(x)
    for x in range(5):
        print(g.vertice_aleatorio())

    return


def pruebas_insertar_aristas():
    print("Pruebas insertar aristas\n")
    g = Grafo()
    g.agregar_vertice(1)
    g.agregar_vertice(2)
    g.agregar_vertice(3)
    g.agregar_vertice(4)
    g.agregar_arista(1,2)
    g.agregar_arista(1,6)
    g.agregar_arista(1,4)
    g.agregar_arista(1,5)
    print("Adyacentes vertice 1: 2-6-4-5")
    g.agregar_arista(5,1)
    print("Adyacentes vertice 5: 1")
    vertices = g.obtener_vertices()
    for x in vertices:
        print("El vertice es ",x,"y sus adyacentes",g.adyacentes(x))
    print("Imprimo lista adyacencia")
    print("Obtener adyacentes aleatorios del 1")
    for x in range(3):
        print(g.adyacente_aleatorio(1))
    g.lista_adyacencia()

def pruebas_grafo():
    print("Comienzo pruebas grafo\n")
    pruebas_grafo_vertices()
    pruebas_insertar_aristas()
    return

def pruebas_pila_apilar():
    print("Pruebas pila apilar\n")
    pila = Pila()
    print("pila vacia")
    print("La pila creada esta vacia",pila.esta_vacia())
    print("No se puede ver tope",pila.ver_tope())
    print("No se puede desapilar",pila.desapilar_valor(None))
    print("Pruebo apilar")
    for x in range(10):
        pila.apilar(x)
    print("La cantidad es 10", pila.cantidad)
    print("El tope es 9: ",pila.ver_tope() == 9)
    for x in range(10):
        ok = (pila.ver_tope() == 9-x)
        pila.desapilar()
        print("Tope correcto: ",9-x,ok)

def pruebas_pila_desapilar():
    print("Prueba pila desapilar\n")
    pila = Pila()
    for x in range(10):
        pila.apilar(x)
    print(pila.elementos())
    print("Prueba eliminar valores")
    print("Elimino el 5: ",pila.desapilar_valor(5) == 5)
    print(pila.elementos())

def pruebas_pila():
    pruebas_pila_apilar()
    pruebas_pila_desapilar()

def prueba_encolar():
    print("Prueba encolar")
    cola = Cola()
    print("Cola vacia",cola.esta_vacia())
    print("Desencolar false",cola.desencolar() == None)
    for x in range(5):
        cola.encolar(x)
        ok = cola.ver_tope() == 0
        print("Tope correcto",ok)
    print(cola.elementos())

def prueba_desencolar():
    print("Pruebas desencolar")
    cola = Cola()
    for x in range(5):
        cola.encolar(x)
    print(cola.elementos())
    print("Elimino el primero en la cola")
    print("El primero es: ",cola.ver_tope())
    cola.desencolar()
    print(cola.elementos())
    print("Elimino el 3 ")
    cola.desencolar_valor(3)
    print(cola.elementos())
    print("Cantidad es:",cola.cantidad)

def pruebas_cola():
    print("Prueba cola\n")
    prueba_encolar()
    prueba_desencolar()


def pruebas_bfs_camino_corto():
    print("Pruebas BFS camino corto\n")
    g = Grafo()
    for x in range(1,11):
        g.agregar_vertice(x)
    g.agregar_arista(1,2)
    g.agregar_arista(1,5)
    g.agregar_arista(2,3)
    g.agregar_arista(2,4)
    g.agregar_arista(5,6)
    g.agregar_arista(5,7)
    g.agregar_arista(7,8)
    g.agregar_arista(7,9)
    camino_corto = bfs_camino_corto(g,1,9)
    print("Para ir de 1-9, el camino es 1-5-7-9")
    print(camino_corto == [1,5,7,9])
    print("Para ir de 1-1, el camino es 1")
    camino_corto1 = bfs_camino_corto(g,1,1)
    print(camino_corto1 == [1])
    print("Para ir de 1-3, el camino es 1-2-3")
    camino_corto2 = bfs_camino_corto(g,1,3)
    print(camino_corto2 == [1,2,3])
    print("Para ir de 1-4, el camino es 1-2-4")
    camino_corto3 = bfs_camino_corto(g,1,4)
    print(camino_corto3 == [1,2,4])
    print("Para ir de 1-8, el camino es 1-5-7-8")
    camino_corto4 = bfs_camino_corto(g,1,8)
    print(camino_corto4 == [1,5,7,8])
    print("Para ir de 3-9, el camino es -1")
    camino_corto5 = bfs_camino_corto(g,3,9)
    print(camino_corto5 == [-1])


def pruebas():
    pruebas_grafo()
    pruebas_pila()
    pruebas_cola()
    pruebas_bfs_camino_corto()
pruebas()

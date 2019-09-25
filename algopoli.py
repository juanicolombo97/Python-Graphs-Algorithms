#!/usr/bin/python3
import sys,string,grafo
from biblioteca import *
from grafo import *

#----------------------------------------------------------
#AUXILIARES

def Segundo(elem):
    return elem[1]

def lista_mas_imp(dicc,largo):
    lista = list(dicc.items())
    lista.sort(key = Segundo)
    lista_nueva = []
    for x in range(int(largo)):
        lista_nueva.append(lista[len(lista)-1-x][0])
    return lista_nueva

def dicc_a_lista(dicc,fin):
    lista = [fin]
    vertice = dicc[fin]
    while vertice != None:
        lista.insert(0,vertice)
        vertice = dicc[vertice]
    return lista
#----------------------------------------------------------
# FUNCIONES QUE UTILIZAN LA BIBLIOTECA PARA REALIZAR LOS PROGRAMAS PEDIDOS
def min_seguimientos(commandos,grafo):
    #Mediante bfs obtiene el camino mas corto de un vertice a otro, recibidos por parametro
    dato = bfs_camino_corto(grafo,commandos[1],commandos[2])
    if dato == -1:
        print("Seguimiento imposible")
        return
    lista = dicc_a_lista(dato,commandos[2])
    return imprimir_flecha(lista)

def mas_impor(grafo,cantidad):
    #Utilizando Random walks obtiene los vertices mas importantes.
    dicc = mas_importantes(grafo,int(cantidad))
    lista = lista_mas_imp(dicc,cantidad)
    return imprimir_lista_coma(lista)

def persecucion(lista,grafo):
    #Devuelve el camino mas corto desde un vertice hasta otro dentro de los lista[largo-1], siendo
    #cantidad de mas_imp recibida por parametro,
    largo = len(lista)
    dicc = mas_importantes(grafo,int(lista[largo-1]))
    l_mas_importante = lista_mas_imp(dicc,lista[largo-1])
    recorrido = []
    for importantes in l_mas_importante:
        for delin in lista[1].split(','):
            dicc_camino= bfs_camino_corto(grafo,delin,importantes)
            lista_cam = dicc_a_lista(dicc_camino,importantes)
            if len(recorrido)==0:
                recorrido = lista_cam
            elif len(lista_cam) < len(recorrido):
                recorrido = lista_cam
    return imprimir_flecha(recorrido)

def divulgar(grafo,v_inicio,profundidad):
    #Devuelve una lista con los delincuentes a los q le llega un mensaje, con distancia
    # al v_inico menor igual a profundidad
    lista = list(bfs_niveles(grafo,v_inicio,int(profundidad)))
    return imprimir_lista_coma(lista)

def divulgar_ciclo(grafo,v_inicio,profundidad):
    #Devuelve una lista que es el camino mas simple desde un v_inico al mismo, distancia
    #igual a profundidad

    padre= dfs(grafo,v_inicio,int(profundidad))
    if padre == -1:
        print("No se encontro recorrido")
        return
    lista = [v_inicio]
    vertice = padre[v_inicio]
    while vertice != lista[0]:
        lista.append(vertice)
        vertice = padre[vertice]
    lista.append(vertice)
    lista.reverse()
    return imprimir_flecha(lista)

def comunidades(grafo,largo):
    lista_communidades = commun(grafo,largo)
    contador=1
    for x in lista_communidades:
        print("COMUNIDAD {}: ".format(contador),end='')
        imprimir_lista_coma(x)
        contador+=1
    return

def c_f_c(grafo):
    #Devuelve las componentes fuertemente conexas
    c = cfc(grafo)
    contador = 1
    for x in c:
        print("CFC {}: ".format(contador),end='')
        imprimir_lista_coma(x)
        contador+=1
    return
#----------------------------------------------------------
# FUNCIONES DE IMPRESION
def imprimir_flecha(lista):
    #Recibe una lista e imprime sus valores seguidos de un ->
    for x in range(len(lista)):
        if x == len(lista)-1:
            print("{}".format(lista[x]))
        else:
            print("{} -> ".format(lista[x]),end="")
    return

def imprimir_lista_coma(lista):
    #Recibe una lista si bool es False, o una lista de tuplas si es True, e imprime los
    #valores seguidos de una coma
    for x in range(len(lista)):

        if x != len(lista)-1:
            print("{}, ".format(lista[x]),end='')
        else:
            print(lista[x])
    return

#----------------------------------------------------------
# FUNCIONES DE MANEJO DE COMANDOS Y ARCHIVO
def procesado_commandos(lista_commandos,grafo):
    programa = lista_commandos[0]
    if programa == 'min_seguimientos':
        min_seguimientos(lista_commandos,grafo)
    elif programa == 'mas_imp':
        mas_impor(grafo,lista_commandos[1])
    elif programa == 'persecucion':
        persecucion(lista_commandos,grafo)
    elif programa == 'divulgar':
        divulgar(grafo,lista_commandos[1],lista_commandos[2])
    elif programa == 'divulgar_ciclo':
        divulgar_ciclo(grafo,lista_commandos[1],lista_commandos[2])
    elif programa == 'cfc':
        c_f_c(grafo)
    elif programa == 'comunidades':
        comunidades(grafo,lista_commandos[1])
    else:
        print("Commandos invalidos")

def pedir_commandos():
    comm = input()
    return comm.split(' ')

def lectura_archivo(archivo):
    g = Grafo()
    with open(archivo,'r') as archivo:
        for linea in archivo:
            v_inicio,v_fin = linea.rstrip('\n').split("\t")
            g.agregar_arista(v_inicio,v_fin)
    return g

#----------------------------------------------------------
# MAIN
def main():
    if len(sys.argv) != 2:
        print("La cantidad de commandos es distinta de 2, ingrese commandos validos")
        return
    grafo = lectura_archivo(sys.argv[1])
    l_commandos = pedir_commandos()
    procesado_commandos(l_commandos,grafo)
    return
main()

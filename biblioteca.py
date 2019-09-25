from grafo import *
from cola import *
from pila import *
import sys

def no_esta(lista,vertice):
    #Se fija si el vertice esta en la lista o no,
    #Si no esta devuelve False, y si esta True
    for x in lista:
        if x[1] == vertice:
            return True
    return False

def bfs_camino_corto(grafo,v_inicio,v_fin):
    #Recibe un vertice de inicio y otro de fin y devuelve el camino mas corto
    #desde el incio al fin utilizando bfs
    cola = Cola()
    padre = {}
    visitados = set()
    visitados.add(v_inicio)
    cola.encolar(v_inicio)
    padre[v_inicio] = None
    while not cola.esta_vacia():
        vertice = cola.desencolar()
        adyacentes = grafo.adyacentes(vertice)
        if adyacentes == None:
            return -1
        for x in adyacentes:
            if x not in visitados:
                padre[x] = vertice
                visitados.add(x)
                cola.encolar(x)
                if x == v_fin:
                    return padre
    return -1

def mas_importantes(grafo,cantidad):
    #Recibe un grafo, y una cantidad y devuelve los cantidad de  vertices mas importantes del grafo,
    # segun el algoritmo de Random Walks
    dicc = {}
    #Para recorrer muchos caminos distintos
    for x in range(3000):
        vertice = grafo.vertice_aleatorio()
        ady = grafo.adyacente_aleatorio(vertice)
        if ady == None:
            continue
        for x in range(150):
            if ady not in dicc:
                dicc[ady]=1
            elif ady in dicc:
                dicc[ady]+=1
            ady = grafo.adyacente_aleatorio(ady)
            if ady == None:
                break
    return dicc

def bfs_niveles(grafo,v_inicio,profundidad):
    #Recibe un v_inico y una profundidad, y utiliza bfs para devolver una lista,
    #con los vertices a una distancia menor igual a profundidad del v_inicio
    distancia = {}
    cola = Cola()
    visitados= set()
    cola.encolar(v_inicio)
    distancia[v_inicio] = 0
    while not cola.esta_vacia():
        vertice = cola.desencolar()
        adyacentes = grafo.adyacentes(vertice)
        if adyacentes == None:
            continue
        for ady in adyacentes:
            if ady == v_inicio:
                continue
            if ady not in visitados:
                distancia[ady] = distancia[vertice]+1
                if distancia[ady] > profundidad:
                    return visitados
                visitados.add(ady)
                cola.encolar(ady)
    return visitados

def dfs(grafo,v_inicio,profundidad):
    #Recibe un v_inicio y una profundidad y encuentra el camino del vertice de inicio al mismo,
    # de largo igual a profundidad
    adyacentes = grafo.adyacentes(v_inicio)
    #Si no tiene adyacentes, no hay camino
    if not adyacentes:
        return -1
    for ady in adyacentes:
        visitados = set()
        padre = {}
        distancia = {}
        distancia[ady]=1
        padre[ady] = v_inicio
        camino =  _dfs(grafo,ady,visitados,padre,distancia,profundidad,v_inicio)
        if camino:
            return camino
    return -1

def _dfs(grafo,vertice,visitados,padre,distancia,prof,v_inicio):
    #Caso de que el camino sea correcto
    if vertice == v_inicio and distancia[vertice] == prof:
        return padre
    #Si llego al largo del camino, pero no entro al anterior significa que el camino tiene el largo,
    #pero no al vertice de inicio, asique ya esta mal
    if distancia[vertice] == prof:
        return None
    #Si el vertice es el de inicio, pero la distancia no es correcta,no es el camino buscado
    if distancia[vertice] != prof and vertice == v_inicio:
        return None
    visitados.add(vertice)
    for ady in grafo.adyacentes(vertice):
        if ady not in visitados:
            padre[ady] = vertice
            distancia[ady]= distancia[vertice] +1
            camino = _dfs(grafo,ady,visitados,padre,distancia,prof,v_inicio)
            #Ya si el camino es correcto lo devolvemos, sino seguimos
            if camino !=None:
                return padre
    visitados.remove(vertice)
    return None

def dfs_cfc(grafo,v,visitados,orden,p1,p2,cfcs,en_cfs):
    visitados.add(v)
    p1.apilar(v)
    p2.apilar(v)
    for w in grafo.adyacentes(v):
        if w not in visitados:
            orden[w] = orden[v] + 1
            dfs_cfc(grafo,w,visitados,orden,p1,p2,cfcs,en_cfs)
        elif w not in en_cfs:
            while orden[p2.ver_tope()] > orden[w]:
                p2.desapilar()
    if p2.ver_tope() == v:
        p2.desapilar()
        z = None
        nueva_cfc = []
        while z != v:
            z = p1.desapilar()
            en_cfs.add(z)
            nueva_cfc.append(z)
        cfcs.append(nueva_cfc)

def cfc(grafo):
    #Recibe un grafo y devuelvo las componente fuertemente conexas, utilizando el algoritmo de Tarjan
    visitados = set()
    orden = {}
    pila1 = Pila()
    pila2 = Pila()
    cfcs = []
    en_cfs = set()
    for v in grafo.obtener_vertices():
        if v not in visitados:
            orden[v]=0
            dfs_cfc(grafo,v,visitados,orden,pila1,pila2,cfcs,en_cfs)
    return cfcs

def max_freq(lista_ady,label):
    l = []
    for ver in lista_ady:
        l.append(label[ver])
    return max(l)

def comunidad_completa(label,largo):
    dicc_communidades = {}
    for ver in label:
        com = label[ver]
        if com in dicc_communidades:
            dicc_communidades[com]+=1
        else:
            dicc_communidades[com] = 1
    integrantes_com = dicc_communidades.values()
    if max(integrantes_com) < largo:
        return False
    return True

def commun(grafo,largo):
    #Encuentra las communidades dentro de un grafo de al menos el largo de integrantes
    label = {}
    contador = 0
    for vertice in grafo.obtener_vertices():
        label[vertice] = contador
        contador+=1
    lista = list(label.keys())
    while not comunidad_completa(label,int(largo)):
        for vertice in lista:
            adyacentes = grafo.adyacentes(vertice)
            if len(adyacentes) == 0:
                continue
            label[vertice] = max_freq(adyacentes,label)
    return crear_communidades(label,largo)

def crear_communidades(label,largo):
    dicc = {}
    lista = []
    for vertice in label:
        comunidad = label[vertice]
        if comunidad in dicc:
            dicc[comunidad].append(vertice)
        else:
            dicc[comunidad] = [vertice]
    for comunidad in dicc:
        if len(dicc[comunidad]) >= int(largo):
            lista.append(dicc[comunidad])
    return lista

from string import *
def main():
    lista = [(7,1),(5,2),(4,7)]
    print("lista sin ins: {}".format(lista))
    lista.sort()
    if len(lista) < 3:
        print("Aa")
    print(len(lista))
    hola = 1
    cola = False
    for x in lista:
        if hola == x[1]:
            cola = True
            break
    print(cola)
    print(lista)
    print(True and True)
    print(False and True)
    print(True and False)
main()

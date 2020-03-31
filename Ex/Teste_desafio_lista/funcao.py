def inserir(lista, *args):
    lista.append(*args)

def ler(lista):
    print(lista)

def desfazer(lista):
    return lista[-1]
    

def refazer(lista1, lista2):
    lista2.append(lista1[-1])
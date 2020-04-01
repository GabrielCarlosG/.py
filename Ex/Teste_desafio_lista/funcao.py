def inserir(lista_de_tarefas, *args):
    lista_de_tarefas.append(*args)
    print()

def ler(lista_de_tarefas):
    print()
    print('Tarefas: ')
    for i in lista_de_tarefas:
        print(f'    {i}')
    print()

def desfazer(lista_de_tarefas, desfazer):
    if not lista_de_tarefas:
        print('Nada a desfazer ')
        print()
        return    
    r_defazer = lista_de_tarefas.pop()
    desfazer.append(r_defazer)
    

def refazer(desfazer, lista_de_tarefas):
    if not desfazer:
        print('Nada para refazer ')
        print()
        return
    
    last_refaz = desfazer.pop()
    lista_de_tarefas.append(last_refaz)
    
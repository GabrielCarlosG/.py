import funcao
lista_de_tarefas = []
desfazer = []
refazer = []

sair = 'N'

while sair == 'N':
    print('#' * 30)
    print('DIGITE:')
    print('[I] para inserir uma tarefa, \n[V] para ver suas tarefas \n[D] para desfazer \n[R] para refazer')    
    print('#' * 30)
    acao = input('\nDigite uma das opções acima: ').upper()

    if acao == 'I':
        tarefa = input('Digite a tarefa que você deseja adicionar: ')
        funcao.inserir(lista_de_tarefas, tarefa)
    elif acao == 'V':
        funcao.ler(lista_de_tarefas)
    elif acao == 'D':
       d = funcao.desfazer(lista_de_tarefas)
       desfazer.append(d)
       lista_de_tarefas.pop()
       funcao.ler(lista_de_tarefas)
    #    funcao.ler(desfazer) serve para ver se estava funcionando
    elif acao == 'R':
        funcao.refazer(desfazer, lista_de_tarefas)
    else:
        print('Digite uma opção válida')

    sair = input('Você deseja sair? (S/N)').upper()

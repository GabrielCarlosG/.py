from dados import produtos, pessoas, lista
def filtra(pessoa):
    if pessoa['idade'] >=  30:
        return True

#filter com lista
nova_lista = filter(lambda x: x>5, lista)
print(list(nova_lista))

#filter com dicionario

# new_produtos = filter(lambda p: p['preco'] > 50, produtos)
# for produto in new_produtos:
#     print(produto)

velho = filter(filtra, pessoas)
for i in velho:
    print(i['nome'])

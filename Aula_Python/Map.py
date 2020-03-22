from dados import produtos, pessoas, lista

# # nova_lista = map(lambda x: x*2, lista)
# nova_lista = [x * 2 for x in lista]
# print(lista)
# print(list(nova_lista))
precos = map(lambda p: p['preco'], produtos)

# for produto in produtos:
#     print(produto)

for preco in precos:
    print(preco)
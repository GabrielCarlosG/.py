from functools import reduce

Carrinho = []

Carrinho.append(('produto 1', 30))
Carrinho.append(('produto 2', 20))
Carrinho.append(('produto 3', 50))
#pode ser feito através da função REDUCE ou da list comprehension abaixo comentada

soma_carrinho = reduce(lambda ac, p: p[1] + ac, Carrinho, 0)
print(soma_carrinho)

# total = [x for x in Carrinho]
# print(sum(total))
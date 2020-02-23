#Isso é um comentario
'''esse
    é
    outro
    comentario
'''
# print('hello','world', 'teste', sep='-', end='')
# print('j','c', 'd', sep='-', end='')
# print('113' , '565', '324',  sep='.', end='-')
# print('03')

# print('para eu conseguir usar "aspas" dentro da Str, precisa ser inverso as aspas que foram abertas.')
# print('ou utilizar uma \'invertida para ignorar as aspas\'')
# print(R'a ultima opção é colocar um \'\   ' no antes da primeira aspa')

# print('carlos', type('carlos'))
# print(22 , type(22))
# print(1.75 , type(1.75))
# print(22 > 18, type(22 > 18))

#Duvida do aluno que o professor tirou, uma simples função para tratar as casas decimais adicionando um ponto quando
#chega na milhar
def formata_preco(valor):
    try:
        import locale
        valor_int = float(valor)
        locale.setlocale(locale.LC_MONETARY, 'pt_BR.UTF-8')
        valor_formatado = locale.currency(valor_int, grouping=True)
        return valor_formatado
    except ValueError:
        # Trate o erro
        raise
 
 
if __name__ == "__main__":
    preco = '25000.28'
    print(formata_preco(preco))
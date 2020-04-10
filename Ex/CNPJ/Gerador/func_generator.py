from random import randint

REGRESSIVOS = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]

def generator_cnpj():
	cnpj = gera()
	cnpj = calcula_digito(cnpj=cnpj, digito=1)
	cnpj = calcula_digito(cnpj=cnpj, digito=2)
	cnpj = f'{cnpj[:2]}.{cnpj[2:5]}.{cnpj[5:8]}/{cnpj[8:12]}-{cnpj[12:]}'
	return cnpj


def gera():
	new_cnpj = ''
	while len(new_cnpj) < 8:
		new_cnpj += str(randint(0, 9))

	new_cnpj += '0001'
	
	return new_cnpj #Retorna um CNPJ com 12 digítos, faltando somente os digitos verificadores

def calcula_digito(cnpj, digito):
    if digito == 1:
        regressivos = REGRESSIVOS[1:]
        novo_cnpj = cnpj
    elif digito == 2:
        regressivos = REGRESSIVOS
        novo_cnpj = cnpj
    else:
        return None

    total = 0
    for indice, regressivo in enumerate(regressivos):
        total += int(novo_cnpj[indice]) * regressivo

    digito = 11 - (total % 11)
    digito = digito if digito <= 9 else 0

    return f'{novo_cnpj}{digito}'


from random import randint
import re

def validate_digit(cnpj):
	pass


def generator_cnpj():
	new_cnpj = ''
	for i in range(0,8):
		if i == 2 or i == 5:
			new_cnpj += '.'
			new_cnpj += str(randint(0,9))
		elif i == 7:
			new_cnpj += str(randint(0,9))
			new_cnpj += '/0001'
		else:
			new_cnpj += str(randint(0,9))
	
	return new_cnpj #Retorna um CNPJ com 12 digítos, faltando somente os digitos verificadores

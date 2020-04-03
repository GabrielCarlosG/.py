import re


def validate(cnpj):
    cnpj = remove_character(cnpj)
    cnpj += str(digits(cnpj))
    return cnpj
    

def remove_character(cnpj):
    cnpj = re.sub(r'[^0-9]','',cnpj)
    return cnpj[0:-2]


def digits(cnpj):
    n = mult_digit(cnpj)
    digit = 11 - (n % 11)
    if digit > 9:
        return 0
    else:
        return digit


def mult_digit(cnpj):
	validate = 0
	for i in range(5, 0, -1):
		if i > 1:
			cnpj = iter(cnpj)
			validate += int(next(cnpj)) * i
		elif i == 1:
			for number in range(9, 0, -1):
				if number > 1:
					validate += int(next(cnpj)) * number
	return validate
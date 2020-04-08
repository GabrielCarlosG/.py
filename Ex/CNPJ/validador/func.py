import re


def validate(cnpj):
    try:
        if is_sequence(cnpj):
            return False
    except:
        return False

    try:
        cnpj = remove_character(cnpj)
        cnpj += str(digits(cnpj))
        cnpj += str(last_digit(cnpj))
        return cnpj
    except:
        return False
    

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


def last_digit(cnpj):
    n = second_digit(cnpj)
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
		else:
			for number in range(9, 0, -1):
				if number > 1:
					validate += int(next(cnpj)) * number
	return validate

def second_digit(cnpj):
    validate = 0
    for i in range(6, 0, -1):
        if i > 1:
            cnpj = iter(cnpj)
            validate += int(next(cnpj)) * i
        else:
            for number in range(9, 0, -1):
                if number > 1:
                    validate += int(next(cnpj)) * number
    
    return validate


def is_sequence(cnpj):
    sequencia = cnpj[0] * len(cnpj)

    if sequencia == cnpj:
        return True
    else:
        return False

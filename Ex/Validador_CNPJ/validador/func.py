import re


def validate(cnpj):
    cnpj = remove_character(cnpj)
    return cnpj
    

def remove_character(cnpj):
    cnpj = re.sub(r'[^0-9]','',cnpj)
    return cnpj[0:-2]



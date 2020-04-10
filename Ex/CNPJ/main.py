import validador.func_validator
import re


cnpj = input('Digite seu CNPJ:  ')


if validador.func_validator.validate(cnpj):
    print(f'O CNPJ: {cnpj} é válido')
else: 
    print(f'O CNPJ: {cnpj} é inválido')
    # print(validador.func_validator.validate(cnpj))


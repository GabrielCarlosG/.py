import validador.func_validator
import Gerador.func_generator
import re


print('V >> para validar um CNPJ\nG >> para gerar um CNPJ\n')
to_do = input('O que deseja fazer?  ').strip().upper()

if to_do == 'V':
    cnpj = input('Digite seu CNPJ:  ')

    clean_cnpj = re.sub(r'[^0-9]','', cnpj)

    if validador.func_validator.validate(cnpj) == clean_cnpj:
        print(f'O CNPJ: {cnpj} é válido')
    else: 
        print(f'O CNPJ: {cnpj} é inválido')
        # print(validador.func_validator.validate(cnpj))
elif to_do == 'G':
    print(Gerador.func_generator.generator_cnpj())
else:
    print('Digite uma opção válida')

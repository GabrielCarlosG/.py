from validador.func import validate
import re


cnpj = '00.516.974/0001-74'
clean_cnpj = re.sub(r'[^0-9]','', cnpj)
print(validate(cnpj),clean_cnpj)

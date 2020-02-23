Cpf = input('Digite seu CPF "APENAS NUMEROS":  ')
New_cpf = []
soma = 0
cont = 9
a = len(New_cpf)
for i in Cpf:
    New_cpf += i
    if cont == 1:
        break
    cont -= 1
for indice, r in enumerate(range(10, 1, -1)):
    n = int(New_cpf[indice])
    mult = r * n
    soma += mult
valid = 11 - (soma % 11)
if valid > 9:
    New_cpf.append(0)
else:
    New_cpf.append(valid)

for indice, r in enumerate(range(11, 1, -1)):
    n = int(New_cpf[indice])
    mult = r * n
    soma += mult
# print(soma)
valid = 11 - (soma % 11)
if valid > 9:
    New_cpf.append(0)
    pass
else:
    New_cpf.append(valid)
    pass

print(New_cpf)
# cpf_valid = join(New_cpf)
# if cpf_valid == Cpf:
#     print(f'O CPF {Cpf} é valido ')
def conferter_numero(valor):
    try:
        valor = int(valor)
        return valor
    except ValueError:
        try:
            valor = float(valor)
            return valor
        except:
            pass

age = conferter_numero(input('digite sua idade: '))

if age >= 18:
    print('você é de maior')
else:
    print('você não é de maior')
    
print('good bye')

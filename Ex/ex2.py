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

n1 = conferter_numero(input('digite a primeira a nota: '))
n2 = conferter_numero(input('digite a segunda nota: '))

media = (n1 + n2) / 2
if n1 >= 6:
    if n2 >= 6:
        print('aprovado')
else:
    if media >= 6:
        print('aprovado')
    else:
        print('reprovado')

print('sua média é {}, resultado da sua n1: {} e n2 {}'.format(media, n1, n2))

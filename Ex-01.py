hora = input('Me informe a hora, sem os minutos:  ')

try:
    hora = int(hora)
    if hora >= 0 and hora <= 11:
        print('Bom dia!')
    elif hora <= 17:
        print('Boa Tarde!')
    elif hora <= 23:
        print('Boa noite!')
    else:
        print('Algo está errado.')
except: #expression as identifier:
    print('não posso te ajudar')
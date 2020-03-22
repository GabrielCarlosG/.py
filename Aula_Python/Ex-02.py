name = input('Me informe o seu primeiro nome: ').strip()

letters = len(name)

if letters <= 4:
    print('seu nome é curto')

elif letters <= 6:
    print('Seu nome é normal')

elif letters > 6:
    print('Seu nome é muito GRANDE') 
    
else:
    print('Deu errado')
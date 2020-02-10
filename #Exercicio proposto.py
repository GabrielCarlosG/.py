#Exercicio1

num1 = input('Digite um número: ')
num2 = input('Digite outro número: ')

try:
    num1 = int(num1)
    num2 = int(num2)

    divnum1 = num1 % 2
    divnum2 = num2 % 2
    if divnum1 == 0 and divnum2 == 0:
        print('Os dois números são pares')
    elif divnum1 == 0:
        print('Somente o Número 1 é par')
    elif divnum2 == 0:
        print('Somente o número 2 é par')
    else:
        print('Nenhum número é PAR')

except:
    print('Por favor, digite somente números inteiros.')
from math import pow, sqrt

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

print('vamos resolver a equação do segudo grau')
print('para isso nos informe A, B e C')
print(' Ax² + bx + c')
print('siga as informações acima')
a = conferter_numero(input("digite o valor de A da equação: "))

if a > 0:
    b = conferter_numero(input('agora digite o valor de B: '))
    c = conferter_numero(input('agora digite o valor de C: '))
    b2 = pow(b, 2)
    delta = b2 - 4*a*c

    if delta > 0:
        Qdelta = sqrt(delta)
        x1 = (-b + Qdelta)/(2*a)
        x2 = (-b - Qdelta)/(2*a)
    elif delta == 0:
        Qdelta = sqrt(delta)
        x1 = (-b + Qdelta)/(2*a)
        x2 = x1            
            
    else:
        print('não existe nos REAIS')
    print(x1)
    print(x2)
    
    
else:
    print('o Valor de A não pode ser igual ou menor que 0')




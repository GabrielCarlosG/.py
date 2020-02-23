def soma(a, b):
    soma = a + b
    print(soma)

def subtr(a, b):
    subtracao = a - b
    print(subtracao)

def div(a, b):
    div = a / b
    print(div)

def mult(a, b):
    mult = a * b
    print(mult)

print()
print('para fazermos uma conta, entre com dois numeros e um operador.')
print('para sair, digite break no operador')

while True:
    print()
    
    a = input('entre com o primeiro numero: ')
    b = input('entre com o segundo numero:')
    op = input('entre com o sinal da operação: ')

    if not a.isnumeric() or not b.isnumeric():
        print('Você precisa digitar um numero')
        continue
    a = int(a)
    b = int(b)

    if op == '+':
        soma(a, b)
    elif op == '-':
        subtr(a, b)
    elif op == '*':
        mult(a, b)
    elif op == '/':
        div(a, b)
    elif op == 'break':
        break
    else:
        print('infelizmente só sei fazer as contas básicas')
    



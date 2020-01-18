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

print('para fazermos uma conta, entre com dois numeros e um sinal.')
a = float(input('entre com o primeiro numero: '))
op = str(input('entre com o sinal da operação: '))
b = float(input('entre com o segundo numero:'))

if op == '+':
    soma(a, b)
elif op == '-':
    subtr(a, b)
elif op == '*':
    mult(a, b)
elif op == '/':
    div(a, b)
else:
    print('infelizmente só sei fazer as contas básicas')
    



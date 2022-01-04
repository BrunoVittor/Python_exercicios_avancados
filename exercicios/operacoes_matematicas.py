num1 = int(input('Digite um número: '))
oper = str(input('''
Escolha o operador
soma =          [+]
subtração =     [-]
multiplicação = [*]
divisão =       [/] 
'''))
num2 = int(input('Digite outro número: '))
if oper == '+':
    resp = num1 + num2
    print(f'Resultado da soma {resp}')
if oper == '-':
    resp = num1 - num2
    print(f'Resultado da subtração {resp}')
if oper == '*':
    resp = num1 * num2
    print(f'Resultado da multiplicação {resp}')
if oper == '/':
    resp = num1 / num2
    print(f'Resultado da divisão {resp}')

# calculadora

num1 = int(input('Digite o 1° número: '))
operador = (input('Digite o operador: '))
num2 = int(input('Digite o 2º número: '))

if operador == '+':
  resultado = num1 + num2
  print(resultado)
elif operador == '*':
  resultado = num1 * num2
  print(resultado)
elif operador == '/':
  resultado = num1 / num2
  print(resultado)
elif operador == '-':
  resultado = num1 - num2
  print(resultado)

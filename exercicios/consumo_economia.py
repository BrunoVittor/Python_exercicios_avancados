def consumo():
  num1 = int(input('Digite o 1º número: '))
  num2 = int(input('Digite o 2º número: '))
  operador = input('Escolha o operqdo +:-:*:/ : ')
  resp = 0
  if operador == '+':
    resp = num1 + num2
  elif operador == '-':
    resp = num1 - num2
  elif operador == '*':
    resp = num1 * num2
  elif operador == '/':
    resp = num1 / num2
  print(f'O consumo foi de {resp} Km/l')
  if resp < 8:
    print('Venda o carro')
  elif 8 < resp < 14:
    print('Econômico')
  elif resp > 8:
    print('Super econômico')


consumo()

def temp_convert(temp):
  f = temp*(9.0/5.0)+32.0
  return f


graus = int(input('Digite os graus Celcius: '))
print(f'Os graus Celcius convertidos em Fahrenheit são: {temp_convert(graus)}')

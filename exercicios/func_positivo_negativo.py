def positivo_negativo():
  num = int(input('Digite um número: '))
  if num < 0:
    valor = -1
  elif num == 0:
    valor = 0
  else:
    valor = 1
  return valor


print(positivo_negativo())

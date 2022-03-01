def maior_menor():
  maior = menor = 0
  cont = 0
  while cont < 5:
    cont += 1
    num = int(input('Digte um número: '))
    if cont == 1:
      maior = menor = num
    else:
      if num > maior:
        maior = num
      elif num < menor:
        menor = num
  print(f'{maior}')


maior_menor()

def soma_algarismos():
  num = int(input('Digite um número: '))
  if num <= 0:
    print('Número inválido')
  else:
    cont = 0
    for c in str(num):
      var = [int(c)]
    # var = [int(c) for c in str(num)] # Opção a ser tulizada como list compreenchions
      for x in var:
        cont += x
    print(cont)


soma_algarismos()

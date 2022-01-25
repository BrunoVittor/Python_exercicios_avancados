# contagem de caracteres

def contagem_caracteres(nome):
  """
  :param nome: valor a ser referenciado pelo usuário
  """

  cont = 1
  caracteres_ordenados = sorted(nome)
  caracter_anterior = caracteres_ordenados[0]

  for c in caracteres_ordenados[1:]:
    if caracter_anterior == c:
      cont += 1
    else:
      print(f'{caracter_anterior}: {cont}')
      caracter_anterior = c
      cont = 1
  print(f'{caracter_anterior}: {cont}')


if __name__ == '__main__':
  contagem_caracteres(input('Digite o nome a ser validado: '))

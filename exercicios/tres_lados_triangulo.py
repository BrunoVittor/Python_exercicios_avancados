lado1 = int(input('Digite o 1º valor: '))
lado2 = int(input('Digite o 2º valor: '))
lado3 = int(input('Digite o 3º valor: '))


def triangulo_verdadeiro():
  if lado1 < (lado2 + lado3):
    print('É um triangulo')
  elif lado2 < (lado1 + lado3):
    print('É um triangulo')
  elif lado3 < (lado1 + lado2):
    print('É um triangulo')
  else:
    print('Não é um triângulo')


def tipo_triangulo():
  if lado1 == lado2 == lado3:
    print('Triângulo equilátero')
  elif lado1 == lado2 or lado2 == lado3 or lado1 == lado3:
    print('Triângulo isóceles')
  elif lado1 != lado2 != lado3:
    print('Triângulo escaleno')


triangulo_verdadeiro()
tipo_triangulo()

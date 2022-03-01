def volume():
  r = 3.141592
  altura = float(input('Digite a altura: '))
  raio = float(input('Digite o raio: '))
  vol = (r * raio * 2) * altura
  print('*****Volume do cilindro *****')
  print(f'O volume do cilindro com altura de {altura} e raio de {raio} é de {vol}')


volume()

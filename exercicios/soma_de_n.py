def soma_numeros(num1, num2):
  acum = 0
  for c in range(num1 + 1, num2):
    acum += c
  print(acum)


num1 = int(input('Digite o 1º número: '))
num2 = int(input('Digite o 2º número: '))
soma_numeros(num1, num2)

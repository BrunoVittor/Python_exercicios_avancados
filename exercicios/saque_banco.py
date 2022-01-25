# Valor do saque realizado
# retornar quantas notas de cada valor serão nescessárias
# notas de 100, 50, 20, 10, 5 ,2 e 1

saque = int(input('Digite o valor do saque: R$ '))

cem = int(saque / 100)
saque = saque - (cem * 100)

cinquenta = int(saque / 50)
saque = saque - (cinquenta * 50)

vinte = int(saque / 20)
saque = saque - (vinte * 20)

dez = int(saque / 10)
saque = saque - (dez * 10)

cinco = int(saque / 5)
saque = saque - (cinco * 5)

um = saque

print('Notas R$100,00 = ', cem)
print('Notas R$ 50,00 = ', cinquenta)
print('Notas R$ 20,00 = ', vinte)
print('Notas R$ 10,00 = ', dez)
print('Notas R$  5,00 = ', cinco)
print('Notas R$  1,00 = ', um)

numero = int(input("Informe um número inteiro: "))
soma = 0
while numero > 0:
    soma = soma + numero % 10
    numero = numero // 10
if numero < 0:
    print('Número inválido')
print(soma)

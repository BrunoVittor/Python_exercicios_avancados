valor = float(input('Valor do produto: R$ '))
desc = valor * 12/100
resp = valor - desc

print(f'O valor com desconto de 12% é de = R$ {resp:.2f}')

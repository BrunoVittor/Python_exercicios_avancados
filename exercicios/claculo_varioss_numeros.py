# soma # quantidade # media # maior # menor # media dos pares # finalizar quando digitar 0

soma = 0
quant = 0
mai = men = 0
while quant < 5:
  num = int(input('Digite um número: '))
  soma += num
  quant += 1
  if quant == 1:
    mai = men = num
  else:
    if num > mai:
      mai = num
    if num < men:
      men = num
  resp = int(input('Quer continuar 1 para sim e 0 para não: '))
  if resp == 0:
    break
print(f'Soma {soma}')
print(f'Quantidade {quant}')
print(f'Maior {mai}')
print(f'Menor {men}')
print(f'Média {soma / quant}')

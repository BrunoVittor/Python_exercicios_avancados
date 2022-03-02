def consumo(km, comb):
  resp = km / comb
  print(f'O consumo foi de {resp:.2f} Km/l')
  if resp < 8:
    print('Venda o carro')
  elif 8 < resp < 14:
    print('Econômico')
  elif resp > 8:
    print('Super econômico')


km = int(input('Digite a kilometragem: '))
comb = int(input('Digite a quantidade de combustível: '))
consumo(km, comb)

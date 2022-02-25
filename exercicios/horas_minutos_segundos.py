def tempo(horas, minutos, segundos):
  calc_horas = horas * 3600
  calc_minutos = minutos * 60
  calc = segundos
  return str(calc_horas + calc_minutos + calc)


horas = int(input('Digite as horas: '))
minutos = int(input('Digite os minutos: '))
segundos = int(input('Digite os segundos: '))
print(f'Os valores convertidos em segundos são {tempo(horas, minutos, segundos)}')

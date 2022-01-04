horas = float(input('Digite o valor das horas trabalhadas: R$ '))
horas_mes = float(input('Digite quantas horas foram trabalhadas no mês: '))
soma_horas = horas * horas_mes
acrescimo = (soma_horas * 10/100) + soma_horas
print(f'{acrescimo:.2f}')

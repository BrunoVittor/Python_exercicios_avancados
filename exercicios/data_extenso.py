import datetime


def data_extenso():
  meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro',
           'Novembro', 'Dezembro']
  dia = int(input('Dia: '))
  mes = int(input('Mês: '))
  ano = int(input('Ano: '))
  return f'Dia {dia}, Mês {meses[mes - 1]}, Ano {ano}'


print(data_extenso())

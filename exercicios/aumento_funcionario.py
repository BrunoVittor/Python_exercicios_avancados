# aumento anual
# contratado em 1995 por R$ 2000,00
# em 1996 aumento de 1.5 %
# a partir de 1997 aumentos são o dobro do anterior
# Qual o salário atual do funcionário ?


from datetime import date

salario = 2000
ano = 1996
porcentagem = 0
while ano < date.today().year:
  ano += 1
  porcentagem += ((porcentagem + salario * (1.5 / 100)) * 2) + salario
print(f'No ano de {ano} o salário é de R$ {porcentagem:.2f}')

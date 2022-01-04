salario = float(input('Digite o slário: R$'))
gratificacao = (salario * 5/100) + salario
desconto = salario - (salario * 7/100)
print(f'Salário com gratificação R${gratificacao:.2f}')
print(f'Salário com imposto R${desconto:.2f}')

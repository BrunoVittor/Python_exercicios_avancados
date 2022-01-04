salario = float(input('Digite o salário: R$'))
emprestimo = float(input('Digite o valor da prestação do empréstimo: R$'))
calc_pres = salario * 20/100
if emprestimo > calc_pres:
    print('emprestimo negado')
else:
    print('Emprestimo aprovado !!!')
print(f'Valor da prestação do emprétimo = {emprestimo:.2f}')

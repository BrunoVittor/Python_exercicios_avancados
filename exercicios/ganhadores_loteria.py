premio = float(780000.00)
g1 = premio * 46/100
g2 = premio * 32/100
g3 = premio - (g1 + g2)
print('O premio de R$ 780.000,00 foi dividido entre 3 ganhadores')
print(f'O ganhador 1 recebeu = R${g1:.2f}\nO ganhador 2 recebeu = R${g2:.2f}\nO ganhador 3 recebeu = R${g3:.2f}')

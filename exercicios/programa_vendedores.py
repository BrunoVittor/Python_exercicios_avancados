valor = float(input('Digite o valor da compra: R$'))
desconto = valor - (valor * 10/100)
parcela = valor / 3
comissao_av = desconto * 5/100
comissao_parc = valor * 5/100
print(f'O valor da compra foi de R${valor:.2f} '
      f'\nO valor das parcelas em 3x fo de R${parcela:.2f} sj '
      f'\nO valor da comissão avista foi de R${comissao_av:.2f} '
      f'\nO valor da comissão parcelada foi de R${comissao_parc:.2f}')

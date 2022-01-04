diaria = float(30.00)
dias = int(input('Quantos dias?: '))
desconto = (diaria * dias) * 8/100
valor = (diaria * dias) - desconto
print(f'O valor das diárias com 8% de desconto é de = R$ {valor:.2f}')

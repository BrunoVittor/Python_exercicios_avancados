idade = int(input('Digite a idade: '))
servico = int(input('Digite o tempo de serviço: '))
if idade >= 65 or servico >= 30 or idade == 60 and servico == 25:
    print(f'A idade é de {idade} e o tempo de serviço é de {servico} está aposentado')
else:
    print('Ainda não está aposentado')

altura = float(input('Digite a altura: '))
sexo = str(input('Digite o sexo [M/F]: ')).upper()
if sexo == 'M':
    peso = (72.7 * altura) - 58
    print(f'Seu peso ideal é de {peso:.2f}')
if sexo == 'F':
    peso = (62.1 * altura) - 44.7
    print(f'Seu peso ideal é de {peso:.2f}')

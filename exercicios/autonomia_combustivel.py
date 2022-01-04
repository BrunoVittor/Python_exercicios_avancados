distancia = int(input('Digite a distância em km: '))
litros = int(input('Digite os litros gastos: '))
consumo = distancia / litros

if consumo < 8:
    print('Venda o carro !')
elif 8 <= consumo <= 14:
    print('Econômico !')
elif consumo > 12:
    print('Super econômico')

# 2. Implementar uma função que retorne verdadeiro se o número for primo
# (falso caso contrário). Testar de 1 a 100.


# 1. Implementar duas funções:
# ▪ Uma que converta temperatura em graus Celsius para Fahrenheit.
# ▪ Outra que converta temperatura em graus Fahrenheit para Celsius.
# Lembrando que:
#     9
# F = _.C 32
#     5

# (0 °C × 9/5) + 32 = 32 °F

# def celcius(graus):
#     resultado = (graus * 9/5) + 32
#     print(resultado)
#
#
# graus = int(input('Graus °C: '))
# celcius(graus)
#
#
# def farhei(graus):
#     resultado = (graus - 32) * 5/9
#     print(resultado)
#
#
# graus = int(input('Graus °F: '))
# farhei(graus)

# perguntas = {
#     'pergunta 1': {
#         'pergunta': 'quanto é 2+2',
#         'opções': {'a': '4', 'b': '8', 'c': '5'},
#         'resposta_certa': 'a'
#     },
#     'pergunta 2': {
#         'pergunta': 'quanto é 2*4',
#         'opções': {'a': '7', 'b': '8', 'c': '6'},
#         'resposta_certa': 'b',
#     },
# }
# print()
# respostas_certas = 0
# for pk, pv in perguntas.items():
#     print(f'{pk} = {pv["pergunta"]}')
#
#     print('Respostas')
#     for rk, rv in pv['opções'].items():
#         print(f'{rk}: {rv}')
#
#     resposta_user = input('Qual é a opção: ')
#     if resposta_user == pv['resposta_certa']:
#         print('Correto !!!\n')
#         respostas_certas += 1
#     else:
#         print('Errou ...\n')
#

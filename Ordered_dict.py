
'''
Módulo Collections: Ordered Dict

Em um dicionário a ordenação de valores não é garantida, ao utilizar order dict sempre será retornado na ordem

Para um dicionário normal ser comparado não importa a ordem, mas sim se os valores são iguais,
utilizando o Orderedcict á sequencia também precisa ser igual
'''


# Em um dicionário a ordem de inserção dos elementos não é garantida
from collections import OrderedDict

dicionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

print(dicionario)

dicionario = OrderedDict({'a': 1, 'b': 2, 'c': 3, 'd': 4})

# print(dicionario)

for chave, valor in dicionario.items():
  print(f'chave = {chave}:valor = {valor}')

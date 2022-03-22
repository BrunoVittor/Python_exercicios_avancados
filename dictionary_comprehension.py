"""
Dictionary Comprehension

Se quisermos criar uma lista:

lista = [1,2,3,4]

Se quisermos criar um dicionário:

dicionário = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

Se quisermos criar uma tupla:

tupla = (1,2,3,4)

Se quisermos criar um conjunto:

conjunto = {1,2,3,4}

Sintaxe:
{chave: valor for valor in iterável}
{chave: valor for cahve, valor in iterável.items()}
"""

dicionário = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
lista = [1, 2, 3, 4]

print({chave: valor for chave, valor in dicionário.items()})

print({num: num for num in dicionário})

res = {num: ('Par' if num % 2 == 0 else 'Ímpar') for num in lista}
print(res)

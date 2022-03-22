"""
Set Comprehension

lista = [, 2, 3, 4, 5]
set = {1, 2, 3, 4, 5}
"""

#exemplo:

numeros = {num for num in range(1, 5)}
print(numeros)

#Exemplo2:

num = {x ** 2 for x in range(10)}
print(num)

#Desafio:

num = {x: x ** 2 for x in range(10)}
print(num)

{1, 2, 3, 4}
{0, 1, 64, 4, 36, 9, 16, 49, 81, 25}
{0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}

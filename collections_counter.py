"""
Módulo colections -  counter

Counter - recebe um iteravél como parâmetro e cria um objeto do tipo Collections Counter que é parecido
com um dicionário, contendo como chave o elemento da lista passada como parâmetro de como calor a quantidade de
ocorrências desse elemento.

from collections import Counter

lista = [1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 5, 5]

nome = ('Bruno dos Santos Vittor')

print(Counter(nome))

print(Counter(lista))

print(nome.most_common(5)) # mostra as 5 palavras com mais repetições

Counter({'o': 4, ' ': 3, 't': 3, 'r': 2, 'n': 2, 's': 2, 'B': 1, 'u': 1, 'd': 1, 'S': 1, 'a': 1, 'V': 1, 'i': 1})
Counter({1: 6, 2: 4, 3: 4, 4: 2, 5: 2})


"""





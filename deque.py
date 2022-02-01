'''
Módulo Colletions - Deque

Pdemos dizer que o módulo deque é uma lista de alto desempenho

'''

from collections import deque

lista = deque('Bruno')

print(lista)

lista.append('Santos')

print(lista)

lista.appendleft('nome')

print(lista)

# removendo elementos

print(lista.pop())  # remove e retorna o ultimo elemento igual a lista

print(lista.popleft())  # remove e retorna o primeiro elemento igual a lista


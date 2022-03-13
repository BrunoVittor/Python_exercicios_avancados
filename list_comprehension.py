"""
List Comprehension

- Utilizando listcomprehension nós podemos gerar novas listas com dados processados a partir de outro iterável

# Sintaxe da List Comprehension

[dado + 1 for contador in itarével]
faça algo para cada dado na coleção de dados

num = [1, 2, 3, 4, 5]
res = [numero * 2 for numero in num]
print(res)

res = [numero / 2 for numero in num]
print(res)


def funcao(valor):
  return valor * valor


res = [funcao(numero) for numero in num]
print(res)

num = [1, 2, 3, 4, 5]
lista = []
for c in num:
  var = c * 2
  lista.append(var)
print(lista)

# formatado em listcomprehensions
print([numero * 2 for numero in num])

"""


def nomes(pessoa):
  pessoa = pessoa.upper()
  return pessoa


amigos = ['Bruno', 'Kamila', 'Caio', 'Thiago']
print([nomes(nome) for nome in amigos])

"""
Conjutos

Quando nos referimos a conjuntos em qualquer linguagem de programação,
estamos fazendo referência á teoria dos conjuntos da matemática.py

Em python os conjuntos são chamados de sets.

- Sets (conjuntos) não possuem valores duplicados:
- Sets (conjuntos) não possuem valores ordenados:
- Elementos não são acessados via índice, ou seja, conjuntos não são indexados:

Os conjuntos em python são referenciados com {}

# Forma 1
s = set({1, 2, 3, 4, 5, 5, 6, 7, 2, 3, 1})

print(s)
print(type(s))

# {1, 2, 3, 4, 5, 6, 7}
# <class 'set'>

# Ao criar um conjunto, caso seja adicionado um valor já existente,
# o mesmo será ignorado sem gerar erros e não fará parte do conjunto

# Forma 2 - mais comum

s = {1, 2, 3, 4, 1, 2} # Para gerar um Set basta adiconar o dado sem chave: valor como é feito no dicionário
print(s)
print(type(s))

# Podemos verificar se determinados elementos existem no conjunto

if 3 in s:
  print('Têm o 3')
else:
  print('Não têm o 3')

# Importante lembrar que, além de não termos valores duplicados, não temos ordem do input,
será sempre ordenado aleatóriamente

# O Set é muito indicado para situações em que queremos eliminar duplicidade de dados

EX:

cidades = ['São Paulo', 'Cuiaba', 'Belo horizonte', 'Rio de Janeiro', 'Cuiaba', 'Belo horizonte', 'São Paulo']

print(set(cidades))
print(len(set(cidades)))

{'São Paulo', 'Cuiaba', 'Belo horizonte', 'Rio de Janeiro'}
4

podemos adicionar elementos em um Set utilizando .add(), duplicidade não gera erro apenas não será adicionado

para remover elementos .remove() ou .discard(), apenas informamos o valor a ser removido

o recurso .union() serve para unificar dois Set em uma única váriavel, o caracter | faz a mesma função do .union() >>> é o método mais recomendado

Ex: alunos = alunos1 | alunos2

{'Kamila', 'Bruno', 'Caio', 'Thiago', 'Isabella'}

alunos1 = {'Bruno', 'Kamila', 'Isabella'}

alunos2 = {'Caio', 'Thiago'}

alunos = alunos1.union(alunos2)

print(alunos)

{'Kamila', 'Bruno', 'Caio', 'Thiago', 'Isabella'}

O recurso .intersection() retorna os valores que estão nos 2 conjuntos:


# Forma 1

alunos1 = {'Bruno', 'Kamila', 'Isabella', 'Renato'}

alunos2 = {'Caio', 'Thiago', 'Isabella', 'Felipe', 'Renato'}

ambos = alunos1.intersection(alunos2)
print(ambos)

{'Renato', 'Isabella'}

# Forma 2

ambos = alunos1 & alunos2

{'Renato', 'Isabella'

Para mostrar os valores que não estão nos 2 conjuntos:

diferenca = alunos1.difference(alunos2

alunos1 = {'Bruno', 'Kamila', 'Isabella', 'Renato'}

alunos2 = {'Caio', 'Thiago', 'Isabella', 'Felipe', 'Renato'}

diferenca = alunos1.difference(alunos2)

diferenca2 = alunos2.difference(alunos1)

print(diferenca)
print(diferenca2)

{'Bruno', 'Kamila'}
{'Thiago', 'Felipe', 'Caio'}

"""
"""
Listas Aninhadas

_ Algumas linguagens de programação possuem uma estrutura de dados chamadas arrays:
  - Unidimensionais (Arrays/Vetores);
  - Multidimenisonais (Matrizes);

"""

# Exemplos:

listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  # matriz 3 x 3

# iterando sobre listas aninhadas
for lista in listas:
  for num in lista:
    print(num)

# list comprehension
[[print(valor) for valor in lista]for lista in listas]

print([['*' for i in range(1, 5)]for c in range(1, 5)])

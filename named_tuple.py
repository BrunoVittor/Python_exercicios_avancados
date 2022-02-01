"""
Módulo collections - Named Tuple

Named Tuple - São tuplas diferenciadas onde especificamos um nome para a mesma e parâmetros


"""

from collections import namedtuple

# precisamos definir o nome e parâmetros

# Forma 1

cachorro = namedtuple('chachorro', 'idade raca nome ')

# Forma 2

cachorro = namedtuple('cchorro', 'idade, raca, nome')

# Forma 3

cachorro = namedtuple('cachorro', ['idade', 'raca', 'nome'])

# Utilização

lucky = cachorro(idade=2, raca='vira-lata', nome='lucky')

print(lucky)

# Acessando dados forma 1

print(lucky[0])
print(lucky[1])
print(lucky[2])

# Acessando dados forma 2

print(lucky.idade)
print(lucky.raca)
print(lucky.nome)



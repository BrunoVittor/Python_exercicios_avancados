"""
Dicionários

obs: em algumas linguagens de programação, dicionários são conhecidos por mapas

Dicionários são coleções chave/valor.

Dionário são representados por chaves {}.

OBS: Chave e valor são separados por :
     Tanto chave quanto valor podem ser qualquer tipo de dados
     Podemos misturar tipos de dados

# Forma 1(mais comum)

paises = {'br': 'Brasil', 'eua': 'Estados unidos', 'pr': 'Paraguai'}
print(paises)
print(type(paises))

# forma 2(menos comum)

paises = dict(br='Brasil', eua='Estados Unidos', pr='Paraguai')
print(paises)
print(type(paises))

A melhor forma de acessar uma chave no dicionário é atraves do .get

ex:

print(paises.get('br'))

Caso seja chamada uma chave que não existe, será retonardo o typo None e não um erro.

O typo None é utilzado quando queremos utilizar um váriavel sem tipo.

O tipo None é sempre considerado como false.

Qualquer valor pode ser utilizado como chave do dicionário (int, bolena, float, string) inclusive listas e tuplas dicionário.

# Como adicionar elementos a um dicionário

receita = {'jan': 100, 'fev': 400, 'mar': 200}

# Forma 1 - mais comum

receita['abr'] = 350

print(receita)
# Forma 2

dado = {'mai': 700}

receita.update(dado) # Ou receita.update({'mai': 700})

print(receita)

# Para adicionar atualizar dados em um dicionário.

# A forma de adicionar e atualizar dados é a mesma
# Em dicionários não podemos ter chaves repetidas.

# Remover dados de um dicionário.

receita = {'jan': 100, 'fev': 400, 'mar': 200}

# Forma 1 - mais comum

ret = receita.pop('mar')

# Obs 1: Aqui precisamos sempre informar a chave, e caso não encontre o elemento, um Keyerror é retornado.
# Obs 2: Ao removermos o valor de um objeto, o valor desse objeto é sempre retornado

# Forma 2

del receita['fev']

# Obs: se  achave não existir, será gerado um keyerror
# Neste caso o valor removido não é retornado.

Quando se utiliza o .clear() todos os dados do dicionário serão deletados



"""


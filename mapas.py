'''

Os mapas em python são o mesmo que dicionários

para iterar sobre um dicionário é o mesmo procedimento de iteração das listas

receita = {'jan': 100, 'fev': 400, 'mar': 200}

for chave in receita:
  print(chave)


for chave in receita.keys():
  print(receita[chave])

print(receita.keys())   # retorna uma lista de chaves
print(receita.values()) # retorna uma lista de valores

print(receita.items())  # irá retornar um dicionário de tuplas

# utilizando desempacotamento de dicionários

for chave, valor in receita.items():
  print(f'chave={chave} e valor={valor}')

Nos dicionários podemos utlizar bibliotecas python para as seguintes operações:

print(sum.values())
print(max.values())
print(min.values())
print(len(receita))

'''
"""
O **kwargs é um parâmetro como outro qualquer, pode ser atribuido com qualquer nome desde que começe com **.
Por convenção se utiliza o **kwargs.

Este é só mais um parâmetro, mas diferente do *args que colocava os valores extras em uma tupla
o **kwargs exige que utilizemos parâmetros nomeados, e transforma esse parâmetro extra num dicionário.

EX:
def habilidades(**kwargs):
  print(kwargs)
habilidades(Bruno='cavaleiro', Kamila='maga', Isabela='Monge')

def cumpriemto_pythonico(**kwargs):
  if 'geek' in kwargs and kwargs['geek'] == 'Python':  # aqui verificamos se existe a chave 'geek' nos kwargs e se a chave tiver o valor de 'Python'
    return 'Comprimento Pythonico'
  else:
    return 'Olá'


print(cumpriemto_pythonico(geek='Python'))
print(cumpriemto_pythonico(geek='olá'))
def minha_funcao(nome, idade, *args, casado=False, **kwargs):
  print(f'{nome} tem {idade} anos')
  print(args)
  if casado:
    print("casado")
  else:
    print('solteiro')
    print(kwargs)


minha_funcao('Bruno', 34)
minha_funcao('Bruno', 35, 1,2,3,4,5)
minha_funcao('Julia', 35, 'a','b','c','d', status='Feliz', agua='sim')
minha_funcao('Bruno', 35, gosta='sim', vai='Não', tem='Tenho')

def mostrar_nomes(**kwargs):
  return f'Nome: {kwargs["nome"]} \n' \
         f'Sobrenome: {kwargs["sobrenome"]}'


nomes = {"nome": 'Bruno', 'sobrenome': 'Vittor'}
print(mostrar_nomes(**nomes))

"""

def soma_tipos(a, b, c):
  print(a + b + c)


tupla = (1, 2, 3)
lista = [1, 2, 3]
conjunto = {1, 2, 3}

soma_tipos(*tupla)
soma_tipos(*lista)
soma_tipos(*conjunto)

dicionario = dict(a=1, b=2, c=3)
soma_tipos(**dicionario)

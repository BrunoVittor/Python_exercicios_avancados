
"""
Módulo Collections - Default Dict

Default Dct - Ao criar um dicionario utiizando-o, nós informamos um valor default, podendo utilizar um lambda para isso.
Esse valor será utilizado sempre que não houver um valor definido. Caso tentemos acessar uma chave que não existe,
essa chave será criada e o valor default será atribuido.

OBS: Lambdas são funções sem nome, que podem ou não receber parâmetros de entrada e retornar valores.


"""
from collections import  defaultdict

dicionario = defaultdict(lambda: 0)

dicionario['curso'] = 'Programação em Python: Essencial'

print(dicionario)
print(dicionario['outro'])
print(dicionario)

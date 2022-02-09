"""
Definindo Funções

- Funções são pequenas partes de código que realizam tarefas específicas;
- Pode ou não receber entradas de dados e retornar uma saída de dados;
- Muito úteis para executar procedimentos similares por repetidas vezes;

Sempre definir o nome da função com letras minusculas separadas por _

- Parãmetos são váriaveis declaradas na definição de uma função
- Argumentos são dados passados durante a execussão de uma função
- A ordem dos parâmetros importa

- Caso utilizemos nomes dos parâmetros nos argumentos para informá-los, odemos utilizar qualquer ordem.
Ex:
def nome(nome, sobrenome):
  return f'Seu nome completo é {nome} {sobrenome}'

print(nome(Bruno, Vittor))
print(nome(nome=Bruno, sobrenome=Vittor))
print(nome(nome=nome, sobrenome=sobrenome))
print(nome(sobrenome=Vittor, nome=Bruno))

com os argumentos nomeados (Keyword Arguments) não importa a ordem dos parâmetros passados



"""


def soma_impares(numero):
  soma = 0
  for n in numero:
    if n % 2 != 0:
      soma += n
  return soma


lista = [1, 2, 3, 4, 5, 6, 7]

print(soma_impares(lista))

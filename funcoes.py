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

def soma_impares(numero):
  soma = 0
  for n in numero:
    if n % 2 != 0:
      soma += n
  return soma


lista = [1, 2, 3, 4, 5, 6, 7]

print(soma_impares(lista))

# Função sem parametro opcional
def exponencial(valor, potencia):
  return valor ** potencia


print(exponencial(4, 2))


# Função com parametro opcional
def exponencial(valor, potencia=2):  # dessa forma se não for passado nenhum valor para o argumento vale o padrão
  return valor ** potencia


print(exponencial(4))
Obs: Em python os parâmetros com valores default (padrão) DEVEM SEMPRE estar ao final da declaração

Para utilizarmos uma função como parâmetro de outra função:

def soma(num1 + num2):
  return num1 + num2

def mat(num1, num2, fun=soma): # fun esta passando como parâmetro da mat a função soma, se nenhum outro parâmetro for utilizado, soma será default
  return fun(num1,num2)

para se utilizar uma variável global dentro de uma função:

total = 0


def increment():
  global total # Avisando que qeremos utilizar a variável global
  total = total + 5
  return total

"""


def calculadora():
  print(
    '******** Calculadora ********\n Operadores \n + soma\n - subtração\n / divisão\n * multiplicação\n ************************')
  valor1 = int(input('Digite o 1º valor: '))
  operador = input('Digite o operador: ')
  valor2 = int(input('Digite o 2º valor: '))
  resultado = 0
  if operador == '+':
    resultado = valor1 + valor2
  elif operador == '-':
    resultado = valor1 - valor2
  elif operador == '*':
    resultado = valor1 * valor2
  elif operador == '/':
    resultado = valor1 / valor2
  return resultado


print(calculadora())

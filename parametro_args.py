"""
O *args é um parâmetro como outro qualquer, pode ser atribuido com qualquer nome desde que começe com *.
Por convenção se utiliza o *args.

O parâmetro *args utilizado numa função, coloca os valores extras informados em um tupla, não esquecer que tuplas são
sempre imutáveis.

EX:
def somando(*args):
    print(sum(args))


somando(1, 3, 4, 5)
como *args podemos fazer tudo o que uma tupla suporta mas dentro de uma função

Para desempacotar uma coleção(lista) podemos fazer dessa forma:

def soma_numeros(*args):
    print(sum(args))


numeros = [1, 2, 3, 4, 5, 6, 7]
soma_numeros(*numeros) Ao atribuir o * na váriavel o python realiza o desempacotamento automáticamente
O * informa que passamos como argumento uma coleção de dados

"""

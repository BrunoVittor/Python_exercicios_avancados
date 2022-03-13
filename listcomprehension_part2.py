"""
List Comprehension part2

Nós podemos adicionar estruturas condicionais lógicas, as nossas listcomprehension

"""

# Ex 1: Separando pares de ímpares

num = [1, 2, 3, 4, 5, 6]
pares = [numero for numero in num if numero % 2 ==0]
impares = [numero for numero in num if numero % 2 !=0]


print(pares)
print(impares)

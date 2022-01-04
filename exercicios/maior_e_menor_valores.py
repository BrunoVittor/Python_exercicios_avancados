contador = 0
maior = menor = 0

while contador <= 10:
    contador += 1
    num = int(input(f'Digite o {contador}º número: '))

    if contador == 1:
        maior = menor = num

    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num

print(f'O maior número foi {maior} e o menor número foi {menor}')

cont = 0
mai = 0
men = 0
result = 1
quant = int(input(f'digite a quantidade de números: '))
while cont < quant:
    num = int(input(f'Digite o {cont + 1}º número: '))
    cont += 1
    if cont == 1:
        mai = men = num
    else:
        if num > mai:
            mai = num
            result = 1
        elif mai == num:
            result += 1
        elif num < men:
            men = num
print(f'O maior número foi {mai}')
print(f'O maior número aparece {result} vezes')

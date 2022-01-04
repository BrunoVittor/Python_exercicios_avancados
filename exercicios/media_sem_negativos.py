cont = 1
acum = 0
while cont <= 10:
    num = int(input('Digite um número: '))
    if num < 0:
        num = 0
        cont += 1
        print('inválido')
    else:
        cont += 1
        acum = acum + num
        media = acum / 10
print(acum)

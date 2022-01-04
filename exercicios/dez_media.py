cont = 1
total = 0
while cont <= 10:
    num = int(input(f'Digite o {cont}º número: '))
    cont = cont + 1
    total = total + num
media = total / 10
print(f'Á média é {media}')

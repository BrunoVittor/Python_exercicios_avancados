cont = 0
num = 0
while cont <= 50:
    cont += 1
    num = num + 2
    if num % 2 == 0:
        print(num)
    else:
        pass
print(f'A soma dos números é {num}')

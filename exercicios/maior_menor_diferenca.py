num1 = int(input('Digite um número: '))
num2 = int(input('Digite um número: '))
if num1 > num2:
    result = 0
    print(f'O maior número é {num1}')
    for c in range(num2+1, num1):
        result = c
        print(result)
else:
    result = 0
    print(f'O maior número é {num2}')
    for c in range(num1+1, num2):
        result = c
        print(result)

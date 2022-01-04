nota1 = float(input('Digite o valor da 1ª nota: '))
nota2 = float(input('Digite o valor da 2ª nota: '))
media = (nota1 + nota2) / 2
if nota1 < 0 or nota1 > 10:
    print('Notas inválidas')
    exit
elif nota2 < 0 or nota2 > 10:
    print('Notas inválidas')
else:
    print(f'A média foi {media}')

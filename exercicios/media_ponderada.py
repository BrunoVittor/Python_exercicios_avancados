nota1 = float(input('Digite a 1ª nota: '))
nota2 = float(input('Digite a 2ª nota: '))
nota3 = float(input('Digite a 3ª nota: '))

nota3 = nota3 * 2
media = (nota1 + nota2 + nota3) / 3

if media >= 60:
    print(f'A média é {media:.2f} Aprovado')
else:
    print('Reprovado')

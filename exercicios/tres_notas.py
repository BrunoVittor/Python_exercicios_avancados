nota1 = float(input('Digite a 1ª nota: '))
nota2 = float(input('Digite a 2ª nota: '))
nota3 = float(input('Digite a 3ª nota: '))

nota1 = nota1 * 2
nota2 = nota2 * 3
nota3 = nota3 * 5

media = (nota1 + nota2 + nota3) / 3
if media <= 2.9:
    print(f'A média foi {media:.2f} Reprovado')
if 3 <= media <= 4.9:
    print(f'A média foi {media:.2f} Recuperação')
if media >= 5:
    print(f'A média foi {media:.2f} Aprovado')

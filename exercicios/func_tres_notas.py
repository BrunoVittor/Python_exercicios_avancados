def notas(nota1, nota2, nota3, leter):
    media = 0
    if leter == 'a':
        media = (nota1 + nota2 + nota3) / 3
    elif leter == 'p':
        nota1 = nota1 / 5
        nota2 = nota2 / 3
        nota3 = nota3 / 2
        media = (nota1 + nota2 + nota3) / 3
    print(media)


nota1 = float(input('Digite a nota1: '))
nota2 = float(input('Digite a nota2: '))
nota3 = float(input('Digite a nota3: '))
leter = input('Digite o tipo a/p: ')

notas(nota1, nota2, nota3, leter)

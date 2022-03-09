def linhas(n):
    var = 2*n-1
    for c in range(n + 1):
        resp = '!' * c
        print(f'{resp}\n')


n = int(input('Quantidade: '))
linhas(n)


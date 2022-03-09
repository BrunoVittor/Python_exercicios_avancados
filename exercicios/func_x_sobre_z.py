def exponenciacao(x, z):
    resp = 0
    for c in range(x, z+1):
        resp = x * c
    acum = resp * x


x = int(input('número: '))
z = int(input('potência: '))
exponenciacao(x, z)

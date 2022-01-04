# Chico 1.50 cresce 2 por ano
# Zé 1.10 cresce 3 por ano

cont = 0
chico = 1.50
ze = 1.10
while ze < chico:
  cont += 1
  chico += 0.02
  ze += 0.03
print(f'Para que Zé seja maior que Chico levará {cont} anos')

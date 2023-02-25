vidas = 1
moedas = 1

i = 0

for vida in vidas and moedas in moedas:
    if vida > 0 or moedas < 1000:
        vidas = vida -1
        moedas = moedas *10
        i = i + 1

print(i)
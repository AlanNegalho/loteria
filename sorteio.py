import random

jogo = list()
print('Loteria! Faça sua aposta')

for i in range(6):
    jogo.append(int(input('Numero: ')))

lista = list(random.sample(range(60),6))

print('Resultado da Loteria')
print(lista)
print('Seu jogo')
print(jogo)
count = 0
for i in lista:
    if i in jogo:
        print(f'Acertou o número: ',end='')
        print(jogo[jogo.index(i)])
        count += 1

if count == len(jogo):
    print('Ganhou')
else:
    print(f'Acertou somente: {count} números')
import os
os.system('cls')
while True:
    try:
        numero = int(input('Digite um número inteiro: '))
        break
    except ValueError:
        print('Valor inválido. Digite um número inteiro.')


lista = []
contador = 0

for i in range(1,numero+1):
    for j in range(2, i+1):
        if i % j == 0:
            contador += 1
    if contador == 2:
        lista.append(i)
    contador = 0
print(f'Os números primos menores que {numero} são: {lista}')






numero = int(input("Digite um número: "))

print("Números primos até", numero, ":")

for i in range(2, numero + 1):
    primo = True

    for j in range(2, i):
        if i % j == 0:
            primo = False
            break

    if primo:
        print(i)
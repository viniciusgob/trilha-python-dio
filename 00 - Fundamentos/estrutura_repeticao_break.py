while True:
    numero = int(input("Informe um número: "))

    if numero == 11:
        break

    if numero % 3 == 0:
        continue

    print(numero)


# for numero in range(100):

#     if numero % 2 == 0:
#         continue

#     print(numero, end=" ")

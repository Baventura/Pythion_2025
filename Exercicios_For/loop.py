# loop para (listas, strings e etc)

for i in range(10):
    print(i)

    # loop wile (executa enquanto condicao for true)
    contador = 0
    while contador < 10:
        print("contando em:", contador)
        contador += 1
    total = int(input("Quantas vezes contar? "))
    contador = 1

    while contador <= total:
        print(f"Contando: {contador}")
        contador += 1    
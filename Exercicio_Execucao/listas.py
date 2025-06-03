# criando uma lispa
frutas = ["uva", "manga", "laranja", "abacate", "Mixirica"]
numeros = [1,2,3,4,5, 2, 3, 5, 4, ]
variados = [1, "dois", 3, "quatro", True]
print(frutas)
# Imprimir por posicao ou valor na lista

print(frutas[-1])
print(frutas[3])
print(numeros)
print(numeros[-1])
print(numeros[2])

# Substituir um valor na lista

frutas[1] = "abacate"
print(frutas)

variados[1] = [2]
print(variados)

# Adicionar valor na lista no final
numeros.append(6)
print(numeros)

# Adiciona valor na posicao determinada
frutas.insert(0,"Cupu")
print(frutas)

frutas.insert(0,"Tomate")
print(frutas)

# como remover um elemento da lista
frutas.remove("Tomate")
print(frutas)

# remove o ultimo elemento da lista
frutas.pop()
print(frutas)

# como contar quantas vezes o valor aparece na lista
print(numeros.count(5))

# Como contar quantas elementos existe na lista
print(len(numeros))

# Ordem alfabetica
frutas.sort()
print(frutas)

# ordem Inversa
numeros.reverse()
print(numeros)








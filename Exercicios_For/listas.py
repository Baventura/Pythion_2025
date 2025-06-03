#criando listas
estados = ["TO", "SP", "RJ"]

print(estados)

print(estados [0])
print(estados [1])
print(estados [2])

estados = ["TO", "SP", "RJ"]
estados.append ("PA") #adiciona item a lista
print (estados)
estados.remove ("PA") #remove item da lista

estados = ["TO", "SP", "RJ"]
for estado in estados:
    print (f"Olá, {estados}!")

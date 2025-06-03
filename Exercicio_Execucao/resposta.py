
lista_marca = [] 

marca1 = input("Digite a primeira marca: ").capitalize
marca2 = input("Digite a segunda marca: ").capitalize
marca3 = input("Digite a terceira marca: ").capitalize
marca4 = input("Digite a quarta marca: ").capitalize

lista_marca.extend([marca1,marca2,marca3,marca4])

buscar_marca = input("Buscar marca: ").capitalize()

print(lista_marca)
print(buscar_marca in lista_marca)

lista_marca = []

marca1 = input("Digite a primeira marca: ")
marca2 = input("Digite a segunda marca: ")
marca3 = input("Digite a terceira marca: ")
marca4 = input("Digite a quarta marca: ")

lista_marca.extend([marca1,marca2,marca3,marca4])

buscar_marca = input("Buscar marca: ").casefold()

lista_nova = ([marca.casefold() for marca in lista_marca ])

print(lista_nova)
print(buscar_marca in lista_nova)




marcas = []


for i in range(4):
    marca = input(f"Digite a {i+1}ª marca de celular: ")
    marcas.append(marca.strip().lower())  
    


print("\nMarcas cadastradas:")
for m in marcas:
    print("-", m.capitalize())


busca = input("\nDigite a marca que deseja buscar: ").strip().lower()


if busca in marcas:
    print("A marca está na lista!")
else:
    print("A marca NÃO está na lista.")
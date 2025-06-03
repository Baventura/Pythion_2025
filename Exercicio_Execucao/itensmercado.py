# Itens de Mercado

# comando para limpar o terminal
import os
os.system("cls")

itensmercado = ["Feijao", "Arroz", "Oleo", "Macarrao", "Ovos"]

itensmercado.remove("Feijao")

itensmercado.remove("Arroz")

itensmercado.insert(1, "cafe")

itensmercado.insert(3, "papel higienico")

itensmercado.insert(4, "refrigerante")

itensmercado.sort()

print(itensmercado)  

import os
os.system("cls")

lista_carros = []

carro1 = input("Digite carro 1: ")
carro2 = input("Digite carro 2: ")
carro3 = input("Digite carro 3: ")

# append Adiciona um elementos por vez 
lista_carros.append(carro1)
lista_carros.append(carro2)
lista_carros.append(carro3)
#  extend adiciona varios itens por vez

# neste caso o comando lower deve ficar acima da lista a ser adicionada

carro2 = carro2.lower()

lista_carros.extend([carro1, carro2, carro3])



# Procurar um elemento dentro da lista
print("golf" in lista_carros)






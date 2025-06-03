# comando para limpar o terminal
import os
os.system("cls")

# criar uma liscta com cinco numes
Nomes = ["Boaventura", "Ronaldo", "Henrique", "Italo", "Kaio" ]


# adicionar mais 3

Nomes.insert(1,"Joao")


Nomes.insert(2,"Paulo")


Nomes.insert(3,"Amanda")

# excluir 2
Nomes.remove("Joao")


Nomes.remove("Paulo")


# Vao colocar em ordem alfabetica
Nomes.sort()

print(Nomes)




#
lista_times = []

time1 = input("Digite time 1: ")
time2 = input("Digite time 2: ")
time3 = input("Digite time 3: ")

time1 = time1.capitalize()
time2 = time2.capitalize()
time3 = time3.capitalize()

lista_times.extend([time1, time2, time3])

buscar_times = input("Digite o nome do time: ")

print(lista_times)
print(buscar_times in lista_times)

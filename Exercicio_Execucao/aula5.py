# #o estudo do for, i, in, range.
# # se eu quiser que o 5 apareca e so adicionar+ 1 ou coloque 1, e o numero final
# for i in range(5):  
#     print(i)
# # contar de 1 a 21 de 2 em 2
# for i in range(0,21,2):
#     print(i)

# n = int(input("Digite um numero: "))
# soma = 0

# for i in range(1,n+1):
#     soma += i
#     print("A soma dos numeros é ", soma)

# palavra = "Pythion"
# for letra in palavra:
#     print(letra)


# lista = []
# for i in range(5):
#     nome = input("Digite um nome: ").capitalize()
#     lista.append(nome)
#     print(f"O nome foi digitado é {nome}")
# print(lista)
# buscar_nome = input("Buscar nome: ").capitalize()
    
# if  buscar_nome in lista:
#     print(f"{buscar_nome} esta na lista")
# else:
#     print(f"{buscar_nome} não na lista")

    #ecercicio com for

# print("Imprimindo a tabuada")


# num = int(input("Digite um numero "))

# for i in range(11):
#     resultado = num * i
#     print(f'{num} * {i} = {resultado}')


# num = 5
# # % é o modulo ou mode, retorna o resto da divisao
# if num % 2 == 0:
#     print('Numero Par')
# else:
#     print("Impar")


# for i in range(1, 101):
#     if i % 2 == 0:
#       print(i)

# lista = [1000, 800, 2000, 2500, 700, 650,999]

# meta = 1000

# for i in lista:
#     if i >=meta:
#         print(i, "Você recebeu o bonus!, Parabéns ")
#     else:
#         print(i, "você nao recebeu o bonus, por favor venda mais um pouco ")

# Classificação de uma escola

# nota = [7.5, 8.0, 6.9, 8.7, 5.3, 4.1, 3.8]
# for i in nota:
#     if i >=7:
#         print(i,("Você está Aprovado!, Parabéns "))
#     elif i >=5:
#         print(i, ("Você está de Recuperação!, Por favor estude mais "))
#     elif i <5:
#         print(i, "Você está Reprovado!, Tente novamento no proximo ano ")

# soma = 0
# for i in range(5):
#     numero = int(input("Digite um numero: "))
#     soma += numero
#     print(f"A soma dos numeros é {soma} ")


user = "admin"
password = 1234

for i in range(1,4):
    usuario = input("Digite seu usuario ")
    senha = int(input("Digite sua senha "))
    if usuario == user and senha == password:
        print("Login bem sucedido ")
        break
    else:
        print(f"Senha incorreta, tentativa  {i} de 3 tentativa ")
else:
    print("Conta Bloqueada")
    




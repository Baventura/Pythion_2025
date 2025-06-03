import os 
os.system ("cls")

lista_produto = ['ipad', 'iphone', 'airpod', 'macbppk']
preco = ['3000', '5000', '800', '10000']

print(lista_produto[0])

dic_produto = {'ipad': 3000, 'iphone': 5000, 'airpod': 800, 'macbook': 10000}

print(dic_produto)

#Encontrar valor no dicionario
print (dic_produto['ipad'])

#Adicionar valor no dicionario

dic_produto['apple watch']= 8000

print(dic_produto)

#Editar valor no dicionario

dic_produto['airpod']= 2000

print(dic_produto)

#Calcular valores dentro do dicionario

dic_produto['iphone' ] = dic_produto['iphone'] * 1.3
print (dic_produto )

#Remover valor da lista

dic_produto.pop('apple watch')
print (dic_produto )

#Adicionar valor no dicionario

dic_produto['apple watch']= 8000
print (dic_produto )

#verificador de produto

if 'iphone' in dic_produto:
     print ('O produto existe')
else:
     print('O produto nao existe')

#Verificador pelo valor do produto

if 3000 in dic_produto.values:
     print ('O produto com esse valor existe')
else:
     print('Nao existe produto com esse valor')



#Cadastro de produto e preco no dicionario
dic_produto ['S25 ultra'] = 6000
print(dic_produto)

#Atualize os valores dos produtos no dicionario com um aumento de 50%

for produto in dic_produto:
     dic_produto[produto] *= 1.5

print(dic_produto)

meus_produtos = {'Mouse': 150, 'Teclado': 200, 'Monitor': 800, 'Gabinete': 500}

# Mostre todos os produtos e seus precos
print(meus_produtos )

# Peça ao usuario o nome de um produto e mostre o preço(se ele existir no dicionário)
produto1 = input("Qual produto voce que verificar? ").capitalize()
if produto1 in meus_produtos:
    print(f'O produto é {produto1}, e custa R${meus_produtos[produto1]}')
else:
    print('Produto nao encontrado')


# Peça o nome de um produto e um novo preço, e atualize o valor no dicionario.
produto2 = input('Qual produto deseja alterar o preço? ').capitalize()
valor2 = float(input('Qual o novo valor que voce deseja? '))
meus_produtos[produto2] = valor2
print (meus_produtos)


# Permita que o usuario adicione um novo produto com seus preco ao dicionario
produto3 = input("Qual produto voce que adicionar? ").capitalize()
valor3 = float(input ('Qual valor voce deseja nesse produto? '))

meus_produtos[produto3] = valor3
print(meus_produtos)

# Solicite o nome de um produto e remova-o do dicionario(caso exista)

remover = input("Qual produto deseja remover? ").capitalize()

if remover in meus_produtos:
    meus_produtos.pop(remover)
    print("Produto removido com sucesso")
    print(meus_produtos)
else:
    print('Produto nao encontrado')

# Crie um dicionario com 10% de desconto aplicado em todos os produtos e precos

for produto in meus_produtos:
    meus_produtos[produto] = meus_produtos[produto] *0.9
print(meus_produtos)
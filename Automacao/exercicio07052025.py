print(meus_produtos)
buscar_produtos = input("Digite um produto")
if buscar_produtos in meus_produtos:
    print(f'O produto é {buscar_produtos} e o valor é', meus_produtos[buscar_produtos])
else:
    print("Produtos nao existente")

# peca o nome de um produto e um novo preco e atualize o valor no dicionario
nome_produto = input("Digite um produto: ")
novo_volor = float(input("Digite o novo valor do produto "))

meus_produtos[nome_produto] = novo_volor
print(meus_produtos)


#permita que o usuario adicione um novo produto com seu preco ao dicionario.

nome_produto = input("Digite um novo produto: ")
valor_produto = float(input("Digite o valor do novo produto: "))

meus_produtos[novo_produto] = valor_produto
print(meus_produtos)

#Solicite o nome de um novo produto e remova-o do dicionario (caso exista).

if remover_produto in meus_produtos:
    meus_produtos.pop(remover_produto)
    print(meus_produtos)
else:
    print("Produtos nao existe")

# Crie um dicionario com 10% de desconto aplicado em todos os precos
# 
for produto in meus_produtos:
    meus+produtos[produto] = meus_produtos[produto] *0.9
    print(meus_produtos)
       


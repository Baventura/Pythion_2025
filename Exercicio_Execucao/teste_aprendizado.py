# Lista de nomes
nomes = []

# Solicita ao usuário um nome
nome_usuario = input("Digite um nome para verificar: ")

# Verifica se o nome está na lista
if nome_usuario in nomes:
    print(f"O nome '{nome_usuario}' está na lista.")
else:
    print(f"O nome '{nome_usuario}' não está na lista.")
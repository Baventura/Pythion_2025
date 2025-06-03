
# primeira aula matheus
nome = "Boaventura"
idade = 53

altura = 1.65


print(nome)
print(idade)
print(altura)

faturamento = 1500
custo = 700
imposto = 0.1
lucro = faturamento - custo - imposto
print(faturamento)
print(custo)
print(imposto)
print(lucro)

#manipulando string

print(f"0 faturamento é {faturamento} , custo é {custo} o imposto é {imposto} e lucro é")

print("0 faturamento é {} , custo é {} o imposto é {} e lucro é{}".format(faturamento, custo, imposto, lucro))

email_cliente = "boaventurao@gmail.com"
# Colocando todas as letras em maiusculas (upper)

email_cliente = email_cliente.upper()
print(email_cliente)

# colocando todos as letras minusculas (lower)
email_cliente = email_cliente.lower()
print(email_cliente)
nome_cliente = "Boaventura Oliveira"

# Colocando a primeira letra do nome maiuscula (capitalize)
nome_cliente = nome_cliente.capitalize()
print(nome_cliente)

# Colocando as primeiras letras do nome em maiusculas (.title)
nome_cliente = nome_cliente.title()
print(nome_cliente)

# Encontrar um caracter no texto
print(nome_cliente.find("u")) # a contagem sempre se inicia com o, 1, 2, 3, 4, 5, ..... (find)
print(email_cliente.find("@"))

# Contar quantos caracteres tem no texto (len)
print(len(nome_cliente))
print(len(email_cliente))

# Pegar um caracter [contar a letra na posicao]
print(nome_cliente[8])

# Pegar um pedaço do texto (pega um pedaço a depender de que lado dos 2 pontos está
#  conta dali para frente ou dali para traz age como uma gangorra)
print(email_cliente[8:])
print(email_cliente[:8])

# Para substituir parte de um texto (muda o email inicial para a opcao de email final) (.replace)
email_cliente = email_cliente.replace("@gmail.com", "@hotmail.com")
print(email_cliente)

# como dividir o texto (.split)
email = "qualquercoisa@gmail.com"
provedor = email.split("@")[1]
print("o provedor do email é", provedor)


nome = "Boaventura Pinheiro de Oliveira"
nome_nome = nome.split()[1]
print(nome_nome)



frase = " Python é uma linguagem MUITO poderosa! Python é incrivel"
frase2 = " Python é uma linguagem MUITO poderosa! Python é incrivel"
# remove os espacos em branco no inicio e no fim da fase
frase = frase.strip()
print(frase)
# transfor a frase em letras minusculas
frase = frase.lower()
print(frase)
# transformar a frase em letras maiuscula
frase = frase.upper()
print(frase)
# colocar apenas as primeira letras das primeiras palavra da frase com a letra maiuscula
frase = frase.capitalize()
print(frase)
#colocar a primeira letra de todas as palavras da frase em maiuscula
frase = frase.title()
print(frase)
# substitituir Pythio por java
frase = frase.replace("Pythion", "java")
print(frase)
# contar quantas vezes o Pythio aparece na frase original
print(len("Pythion"))


# encontrar a posicao da palavra poderosa
print(frase2.find("poderosa")) # a contagem sempre se inicia com o, 1, 2, 3, 4, 5, ..... (find)





# # Senha correta (substitua pela senha real do Senac)
# senha_correta = "senhasenac"

# # Loop para solicitar e verificar a senha
# while True:
#     # Solicita a senha ao usuário
#     senha_digitada = input("Digite a senha: ")

#     # Verifica se a senha digitada é igual à senha correta

#     if senha_digitada == senha_correta:
#         print("Senha correta! Acesso permitido.")
#         break  # Sai do loop se a senha estiver correta
#     else:
#         password = input("Acesso Negado, Digite a senha novamente: ")

# soma = 0
# while True:
#     numero = float(input("Digite um numero para somar ou 0 para sair: ")) # 
#     if numero == 0: # if significa se
#         break
#     soma += numero # += significa soma = soma + numero
#     print(soma)
# print(f"A soma de todos os numeros digitados é {soma}")     


while True:
    idade = int(input("Digite sua idade: "))
    if idade >=18:
        print("Acesso a festa concedido ")
    else:
        print("ENTRADA PROIBIDA ")
    continuar = input("Deseje verificar mais alguma idade [S OU N]: ").upper()
        
    if continuar == "N":

        break
print("Fim da verificação")


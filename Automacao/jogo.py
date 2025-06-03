# Pedra Papel e Tesoura

import random
# Opcoes jogaveis
opcoes = ["pedra", "papel", "tesousa"]


print("Bem-vindo ao Pedra, Papel ou Tesoura")
print("Escolha uma das opicoes: pedra, papel ou tesoura.")
# Solicite a escolha do jogador
jogador = input("Sua escolha: ").lower()

# Escolha aleatoria do computador
computador = random.choice(opcoes)

print(f"Compuador escolheu: {computador}")
if jogador == computador:
    print ("Empate")
elif (jogador == "pedra" and computador == "tesoura") or\
    (jogador == "papel" and computador == "pedra") or\
    (jogador == "tesoura" and computador == "papel"):
    print ("Voce Venceu!")
elif jogador in opcoes:
    print ("Voce perdeu!")
else:
    print ("Escolha inválida! Tente novamente.")
    


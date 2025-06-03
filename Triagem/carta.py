
import random

def distribuir_cartas():    
    cartas = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10,11]
    return random.choice(cartas)
def ajustar_ace(mao):

    #ajusta o valor do as (11) para 1, se necessario

    while sum(mao) > 21 and 11 in mao:
        mao.remove(11)
        mao.append(1)
    return mao
                   

jogador = [distribuir_cartas(), distribuir_cartas()]
comutador = [distribuir_cartas()]
print(f"Suas cartas: {jogador}") [Total: {sua(jogador)}]


    #jogador compra cartas
while sum(jogador) < 21 and input("Quer outra carta").lower() =="s":
        jogador.append(distribuir_cartas())
        jogador = ajustar_ace(jogador)
        
        print (f"Cartas: {jogador} (Total: {sum (jogador)})")
    #resultado
total_j = sum (jogador)
total_c = sum (computador)

print(f"\nVoce: {jogador} = {total_j}")
print(f"Computador: {comutador} = {total_c}")

if total_j > 21:
        print ("Estorou! Voce Perdeu")
elif total_c > 21 or total_j > total_c:
        print("Voce ganhou ")
elif total_j == total_c:
        print ("Empate! ")
else:
        print("Computador ganhou! kkk")


                   
                              
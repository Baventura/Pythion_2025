# joguinho da forca
import random
palvras = ["python", "programacao", "ronaldo"]
palavra_secreta = random.choice(palvras)
letras_corretas = []
vidas = 6
print("jogo da Forca - Adivinha a palavra")
while vidas > 0:
    #mostrar a palavra oculta
    palavra_oculta = ""
    for letra in palavra_secreta:
        palavra_oculta += letra if letra in letras_corretas else "_"
        print(palavra_oculta)

        #Verifique se ganhou
    if "_" not in palavra_oculta:
        print ("Voce venceu!")
        break
        #Pede uma letra
    tentativa = input ("Digite uma letra:").lower()
    if tentativa in letras_corretas:
        print("Voce ja tentou esta letra!")
    elif tentativa in palavra_secreta:
        letras_corretas.append(tentativa)
        print("Acertou!")
    else:
        vidas -= 1
        print(f"Errou! x Vidas restante: {vidas}")
    if vidas == 0:
        print(f"Perdeu! A palavra era: {palavra_secreta}")



        
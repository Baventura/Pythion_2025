import random
import os
import platform

# Função para limpar a tela
def limpar_tela():
    sistema = platform.system()
    if sistema == "Windows":
        os.system('cls')  # Para Windows
    else:
        os.system('clear')  # Para Linux/MacOS

# Lista de palavras
palavras = ["python", "programacao", "openai", "jogos"]

# Escolhe uma palavra aleatória
palavra_secreta = random.choice(palavras)

# Inicializa variáveis
letras_corretas = []
vidas = 6

# Função para desenhar o boneco da forca
def desenha_forca(vidas):
    fases = [
        """
         ------
         |    |
              |
              |
              |
              |
              |
        ---------
        """,
        """
         ------
         |    |
         O    |
              |
              |
              |
              |
        ---------
        """,
        """
         ------
         |    |
         O    |
         |    |
              |
              |
              |
        ---------
        """,
        """
         ------
         |    |
         O    |
        /|    |
              |
              |
              |
        ---------
        """,
        """
         ------
         |    |
         O    |
        /|\\   |
              |
              |
              |
        ---------
        """,
        """
         ------
         |    |
         O    |
        /|\\   |
        /     |
              |
              |
        ---------
        """,
        """
         ------
         |    |
         O    |
        /|\\   |
        / \\   |
              |
              |
        ---------
        """
    ]
    print(fases[6 - vidas])

# Limpa a tela no início do jogo
limpar_tela()

# Inicia o jogo
print("Jogo da Forca - Adivinhe a palavra!\n")

while vidas > 0:
    # Mostra a palavra oculta
    palavra_oculta = ""
    for letra in palavra_secreta:
        palavra_oculta += letra if letra in letras_corretas else "_ "

    print(f"Palavra: {palavra_oculta}")
    desenha_forca(vidas)  # Desenha a forca com base nas vidas restantes

    # Verifica se o jogador ganhou
    if "_" not in palavra_oculta:
        print("Você venceu! 🏆")
        break

    # Pede uma letra ao jogador
    tentativa = input("Digite uma letra: ").lower()

    # Verifica se a entrada é válida
    if not tentativa.isalpha() or len(tentativa) != 1:
        print("Por favor, digite uma única letra válida.\n")
        continue

    # Verifica se a letra já foi tentada
    if tentativa in letras_corretas:
        print("Você já tentou essa letra!\n")
    elif tentativa in palavra_secreta:
        letras_corretas.append(tentativa)
        print("Acertou! ✅\n")
    else:
        vidas -= 1
        print(f"Errou! ❌ Vidas restantes: {vidas}\n")

# Se o jogador perdeu
if vidas == 0:
    print(f"Perdeu! A palavra era: {palavra_secreta}")
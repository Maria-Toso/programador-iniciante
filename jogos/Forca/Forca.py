import random

def jogar():
    print("*********************************")
    print("*** Bem-vindo ao Jogo da Forca! ***")
    print("*********************************")

    # Lista de palavras para o jogo
    palavras = ["python", "programacao", "computador", "algoritmo", "desenvolvedor", "teclado"]
    
    # Escolhe uma palavra aleatória da lista
    palavra_secreta = random.choice(palavras).upper()
    
    # Cria a visualização da palavra com underscores _
    letras_acertadas = ["_" for letra in palavra_secreta]
    
    enforcou = False
    acertou = False
    erros = 0
    letras_tentadas = []

    # Ciclo principal do jogo
    while(not enforcou and not acertou):

        print(f"\nPalavra: {' '.join(letras_acertadas)}")
        print(f"Letras já tentadas: {', '.join(letras_tentadas)}")
        
        chute = input("Qual a letra? ").strip().upper()

        if chute in letras_tentadas:
            print("Já tentaste essa letra! Tenta outra.")
            continue

        letras_tentadas.append(chute)

        if chute in palavra_secreta:
            # Se a letra estiver correta, substitui o _ na posição certa
            index = 0
            for letra in palavra_secreta:
                if chute == letra:
                    letras_acertadas[index] = letra
                index += 1
        else:
            erros += 1
            desenha_forca(erros)

        enforcou = erros == 6
        acertou = "_" not in letras_acertadas

    if acertou:
        print("\nParabéns, tu ganhaste!")
    else:
        print(f"\nInfelizmente perdeste. A palavra era: {palavra_secreta}")

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
    if(erros == 2):
        print(" |      (_)   ")
        print(" |       |    ")
    if(erros == 3):
        print(" |      (_)   ")
        print(" |      /|    ")
    if(erros == 4):
        print(" |      (_)   ")
        print(" |      /|\   ")
    if(erros == 5):
        print(" |      (_)   ")
        print(" |      /|\   ")
        print(" |      /     ")
    if(erros == 6):
        print(" |      (_)   ")
        print(" |      /|\   ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")

if __name__ == "__main__":
    jogar()

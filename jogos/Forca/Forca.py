import random

def carregar_palavras():
    """Lê as palavras do ficheiro externo e devolve uma lista."""
    palavras = []
    try:
        with open("palavras.txt", "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                palavras.append(linha.strip().upper())
    except FileNotFoundError:
        print("Erro: O ficheiro 'palavras.txt' não foi encontrado!")
        return ["PYTHON"] # Palavra padrão caso o arquivo falte
    return palavras

def selecionar_palavra(nivel):
    """Filtra as palavras com base no nível escolhido."""
    todas_as_palavras = carregar_palavras()
    
    if nivel == 1: # Fácil
        lista_filtrada = [p for p in todas_as_palavras if len(p) <= 5]
    elif nivel == 2: # Médio
        lista_filtrada = [p for p in todas_as_palavras if 6 <= len(p) <= 8]
    else: # Difícil
        lista_filtrada = [p for p in todas_as_palavras if len(p) > 8]

    # Se a lista filtrada estiver vazia, usa qualquer uma
    return random.choice(lista_filtrada if lista_filtrada else todas_as_palavras)

def jogar():
    print("*********************************")
    print("*** Jogo da Forca Profissional ***")
    print("*********************************")

    print("(1) Fácil (2) Médio (3) Difícil")
    escolha = int(input("Escolha o nível: "))
    
    palavra_secreta = selecionar_palavra(escolha)
    letras_acertadas = ["_" for _ in palavra_secreta]
    
    erros = 0
    tentativas = []

    while True:
        print(f"\nPalavra: {' '.join(letras_acertadas)}")
        print(f"Letras tentadas: {', '.join(tentativas)}")
        
        chute = input("Letra: ").strip().upper()

        if chute in tentativas:
            print("Já tentaste essa!")
            continue

        tentativas.append(chute)

        if chute in palavra_secreta:
            for i, letra in enumerate(palavra_secreta):
                if chute == letra:
                    letras_acertadas[i] = letra
        else:
            erros += 1
            desenha_forca(erros)

        if "_" not in letras_acertadas:
            print(f"\nGanhaste! A palavra era {palavra_secreta}")
            break
        if erros == 6:
            print(f"\nPerbeste! A palavra era {palavra_secreta}")
            break

def desenha_forca(erros):
    # (O código da arte ASCII permanece o mesmo da versão anterior)
    print("  _______     ")
    print(" |/      |    ")
    if erros >= 1: print(" |      (_)   ")
    if erros == 2: print(" |       |    ")
    if erros == 3: print(" |      /|    ")
    if erros >= 4: print(" |      /|\   ")
    if erros == 5: print(" |      /     ")
    if erros >= 6: print(" |      / \   ")
    print(" |            ")
    print("_|___         ")

if __name__ == "__main__":
    jogar()

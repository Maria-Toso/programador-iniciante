import os
import shutil

def organizar_pasta(caminho_da_pasta):
    # 1. Definir o mapeamento de extensões para pastas
    formatos = {
        "Imagens": [".jpg", ".jpeg", ".png", ".gif", ".svg"],
        "Documentos": [".pdf", ".docx", ".txt", ".xlsx", ".pptx", ".csv"],
        "Audio": [".mp3", ".wav", ".flac"],
        "Videos": [".mp4", ".mkv", ".mov", ".avi"],
        "Compactados": [".zip", ".rar", ".7z"],
        "Executaveis": [".exe", ".msi", ".dmg"]
    }

    # Mudar o diretório de trabalho para a pasta alvo
    os.chdir(caminho_da_pasta)

    # 2. Listar todos os ficheiros na pasta
    lista_ficheiros = os.listdir()

    contador = 0

    for ficheiro in lista_ficheiros:
        # Ignorar se for uma pasta ou o próprio script
        if os.path.isdir(ficheiro) or ficheiro == "organizador.py":
            continue

        # Extrair a extensão do ficheiro (ex: .pdf)
        nome, extensao = os.path.splitext(ficheiro)
        extensao = extensao.lower()

        # 3. Verificar em qual categoria o ficheiro se encaixa
        movido = False
        for pasta, extensoes_permitidas in formatos.items():
            if extensao in extensoes_permitidas:
                # Criar a pasta se ela não existir
                if not os.path.exists(pasta):
                    os.makedirs(pasta)
                
                # Mover o ficheiro
                shutil.move(ficheiro, os.path.join(pasta, ficheiro))
                print(f"Movido: {ficheiro} -> {pasta}")
                contador += 1
                movido = True
                break
        
        # Opcional: Criar uma pasta "Outros" para extensões desconhecidas
        if not movido:
            if not os.path.exists("Outros"):
                os.makedirs("Outros")
            shutil.move(ficheiro, os.path.join("Outros", ficheiro))
            print(f"Movido: {ficheiro} -> Outros")
            contador += 1

    print(f"\nSucesso! {contador} ficheiros foram organizados.")

if __name__ == "__main__":
    # Pode colocar o caminho completo da pasta que queres organizar aqui
    # Exemplo: "C:/Users/Utilizador/Downloads" ou "." para a pasta atual
    pasta_alvo = input("Digita o caminho da pasta que queres organizar (ou '.' para a atual): ")
    organizar_pasta(pasta_alvo)

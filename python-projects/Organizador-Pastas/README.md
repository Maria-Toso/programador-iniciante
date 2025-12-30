# Organizador de Pastas Automático

Um script em Python que organiza ficheiros desordenados em subpastas categorizadas por tipo de ficheiro.

### Como funciona:
O script analisa a extensão de cada ficheiro num diretório especificado e move-o para a pasta correspondente:
- **Imagens**: .jpg, .png, .gif...
- **Documentos**: .pdf, .docx, .txt...
- **Vídeos**: .mp4, .mkv...
- E outros tipos customizáveis no dicionário do código.

### Ferramentas utilizadas:
- **Biblioteca `os`**: Para manipulação de diretórios e caminhos.
- **Biblioteca `shutil`**: Para operações de movimentação de ficheiros.

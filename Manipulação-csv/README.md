# 📊 Processador Básico de Dados CSV em Python

Este projeto demonstra o uso do módulo nativo `csv` do Python para manipulação de arquivos de dados.

## Funcionalidades

* **Leitura de Dados:** Utiliza `csv.DictReader` para ler o arquivo `data.csv`, tratando a primeira linha como cabeçalho de dicionário.
* **Processamento:** Calcula o `Preço Total` multiplicando `Preco Unitario` por `Quantidade`.
* **Escrita de Dados:** Utiliza `csv.DictWriter` para criar um novo arquivo `output_data.csv` com a nova coluna de resultados.

## Como Executar

1. **Pré-requisitos:** Python 3 instalado.
2. **Execute:** No terminal, navegue até o diretório e execute:
   ```bash
   python processador-csv.py

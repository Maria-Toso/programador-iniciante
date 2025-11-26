import csv
import os

def processar_dados_csv(input_filename, output_filename):
    """
    Lê um arquivo CSV, calcula o Preço Total e salva o resultado em um novo arquivo.
    """
    dados_processados = []
    
    try:
        with open(input_filename, mode='r', newline='', encoding='utf-8') as infile:
            reader = csv.DictReader(infile)
            fieldnames = reader.fieldnames + ['Preco Total']

            for row in reader:
                try:
                    preco_unitario = float(row['Preco Unitario'])
                    quantidade = int(row['Quantidade'])
                   
                    preco_total = preco_unitario * quantidade                    
                    row['Preco Total'] = f"{preco_total:.2f}"
                    dados_processados.append(row)
                    
                except ValueError as e:
                    print(f"Erro de conversão em uma linha: {row}. Erro: {e}")
        
                    
    except FileNotFoundError:
        print(f"ERRO: Arquivo de entrada '{input_filename}' não encontrado. Certifique-se de que ele existe.")
        return

    if dados_processados:
        try:
            with open(output_filename, mode='w', newline='', encoding='utf-8') as outfile:
                writer = csv.DictWriter(outfile, fieldnames=fieldnames)  
                writer.writeheader()                
                writer.writerows(dados_processados)
                
            print(f"\nSucesso! O arquivo de saída foi criado: '{output_filename}'")
            print(f"Total de {len(dados_processados)} linhas processadas.")
            
        except Exception as e:
            print(f"Ocorreu um erro ao escrever o arquivo: {e}")

if __name__ == "__main__":
    INPUT = 'data.csv'
    OUTPUT = 'output_data.csv'
    
    if os.path.exists(INPUT):
        processar_dados_csv(INPUT, OUTPUT)
    else:
        print(f"O arquivo '{INPUT}' não foi encontrado. Certifique-se de que está no mesmo diretório.")

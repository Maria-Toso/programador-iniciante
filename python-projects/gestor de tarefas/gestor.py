import os

# Nome do ficheiro onde as tarefas serão guardadas
FICHEIRO_DADOS = "tarefas.txt"

def carregar_tarefas():
    """Lê as tarefas do ficheiro de texto e coloca numa lista."""
    tarefas = []
    if os.path.exists(FICHEIRO_DADOS):
        with open(FICHEIRO_DADOS, "r", encoding="utf-8") as f:
            for linha in f:
                tarefas.append(linha.strip())
    return tarefas

def guardar_tarefas(tarefas):
    """Guarda a lista de tarefas atual no ficheiro de texto."""
    with open(FICHEIRO_DADOS, "w", encoding="utf-8") as f:
        for tarefa in tarefas:
            f.write(tarefa + "\n")

def mostrar_menu():
    print("\n--- GESTOR DE TAREFAS ---")
    print("1. Ver tarefas")
    print("2. Adicionar tarefa")
    print("3. Remover tarefa")
    print("4. Sair")
    return input("Escolha uma opção: ")

def main():
    tarefas = carregar_tarefas()
    
    while True:
        opcao = mostrar_menu()
        
        if opcao == "1":
            print("\nSUAS TAREFAS:")
            if not tarefas:
                print("A lista está vazia.")
            for i, tarefa in enumerate(tarefas, 1):
                print(f"{i}. {tarefa}")
        
        elif opcao == "2":
            nova_tarefa = input("Digite a nova tarefa: ")
            tarefas.append(nova_tarefa)
            guardar_tarefas(tarefas)
            print("Tarefa adicionada com sucesso!")
            
        elif opcao == "3":
            if not tarefas:
                print("Nada para remover.")
                continue
            try:
                indice = int(input("Digite o número da tarefa a remover: ")) - 1
                removida = tarefas.pop(indice)
                guardar_tarefas(tarefas)
                print(f"Tarefa '{removida}' removida!")
            except (ValueError, IndexError):
                print("Número inválido! Tente novamente.")
                
        elif opcao == "4":
            print("A sair... Até logo!")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()

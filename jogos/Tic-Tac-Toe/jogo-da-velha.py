import tkinter as tk
from tkinter import messagebox

class JogoDaVelha:
    def __init__(self, root):
        self.root = root
        self.root.title("Jogo da Velha - Portfólio")
        
        # Definir o jogador inicial
        self.jogador_atual = "X"
        # Criar o tabuleiro como uma lista de 9 posições vazias
        self.tabuleiro = [""] * 9
        
        self.botoes = []
        self.criar_tabuleiro_ui()

    def criar_tabuleiro_ui(self):
        """Cria a grelha de 3x3 botões."""
        for i in range(9):
            # O comando lambda é usado para passar o índice do botão para a função
            botao = tk.Button(self.root, text="", font=("Helvetica", 20, "bold"), 
                              width=5, height=2, 
                              command=lambda i=i: self.clique_botao(i))
            
            # Organiza em 3 linhas e 3 colunas
            botao.grid(row=i//3, column=i%3)
            self.botoes.append(botao)

        self.botao_reset = tk.Button(self.root, text="Reiniciar Jogo", command=self.reset_jogo)
        self.botao_reset.grid(row=3, column=0, columnspan=3, sticky="nsew")

    def clique_botao(self, indice):
        """Lógica de quando um botão é clicado."""
        if self.tabuleiro[indice] == "" and self.jogador_atual:
            # Marcar no tabuleiro e na interface
            self.tabuleiro[indice] = self.jogador_atual
            self.botoes[indice].config(text=self.jogador_atual, 
                                       fg="blue" if self.jogador_atual == "X" else "red")
            
            if self.verificar_vitoria():
                messagebox.showinfo("Fim de Jogo", f"O jogador {self.jogador_atual} venceu!")
                self.reset_jogo()
            elif "" not in self.tabuleiro:
                messagebox.showinfo("Fim de Jogo", "Empate! Deu velha.")
                self.reset_jogo()
            else:
                # Alternar jogador
                self.jogador_atual = "O" if self.jogador_atual == "X" else "X"

    def verificar_vitoria(self):
        """Verifica todas as combinações possíveis de vitória."""
        vitorias = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8), # Linhas
            (0, 3, 6), (1, 4, 7), (2, 5, 8), # Colunas
            (0, 4, 8), (2, 4, 6)             # Diagonais
        ]
        for a, b, c in vitorias:
            if self.tabuleiro[a] == self.tabuleiro[b] == self.tabuleiro[c] != "":
                return True
        return False

    def reset_jogo(self):
        """Limpa o tabuleiro para uma nova partida."""
        self.tabuleiro = [""] * 9
        self.jogador_atual = "X"
        for botao in self.botoes:
            botao.config(text="", bg="SystemButtonFace")

if __name__ == "__main__":
    root = tk.Tk()
    JogoDaVelha(root)
    root.mainloop()

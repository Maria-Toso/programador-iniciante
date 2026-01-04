import tkinter as tk
from tkinter import messagebox
import random

class JogoForcaGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Jogo da Forca - Versão Visual")
        self.root.geometry("600x500")
        
        self.reiniciar_jogo()

    def carregar_palavra(self):
        try:
            with open("palavras.txt", "r", encoding="utf-8") as f:
                palavras = [linha.strip().upper() for linha in f]
            return random.choice(palavras)
        except:
            return "PYTHON"

    def reiniciar_jogo(self):
        # Limpar interface se já existir
        for widget in self.root.winfo_children():
            widget.destroy()

        # Lógica do Jogo
        self.palavra_secreta = self.carregar_palavra()
        self.letras_acertadas = ["_" for _ in self.palavra_secreta]
        self.erros = 0
        self.tentativas = []

        # Interface
        self.setup_ui()

    def setup_ui(self):
        self.label_palavra = tk.Label(self.root, text=" ".join(self.letras_acertadas), font=("Helvetica", 30))
        self.label_palavra.pack(pady=20)

        self.canvas = tk.Canvas(self.root, width=200, height=200, bg="white")
        self.canvas.pack()
        self.desenhar_estrutura_forca()

        self.frame_entrada = tk.Frame(self.root)
        self.frame_entrada.pack(pady=20)
        
        tk.Label(self.frame_entrada, text="Digite uma letra:", font=("Helvetica", 12)).pack(side=tk.LEFT)
        self.entrada = tk.Entry(self.frame_entrada, width=5, font=("Helvetica", 12))
        self.entrada.pack(side=tk.LEFT, padx=10)
        self.entrada.bind('<Return>', lambda e: self.verificar_letra())

        self.botao = tk.Button(self.frame_entrada, text="Tentar", command=self.verificar_letra, bg="#4CAF50", fg="white")
        self.botao.pack(side=tk.LEFT)

        self.label_status = tk.Label(self.root, text="Boa sorte!", fg="blue")
        self.label_status.pack()

    def desenhar_estrutura_forca(self):
        self.canvas.create_line(20, 180, 180, 180, width=3) 
        self.canvas.create_line(50, 180, 50, 20, width=3)   
        self.canvas.create_line(50, 20, 120, 20, width=3)   
        self.canvas.create_line(120, 20, 120, 40, width=3)  

    def desenhar_boneco(self):
        if self.erros == 1: 
            self.canvas.create_oval(100, 40, 140, 80, width=3) 
        elif self.erros == 2: 
            self.canvas.create_line(120, 80, 120, 130, width=3) 
        elif self.erros == 3: 
            self.canvas.create_line(120, 90, 90, 110, width=3)  
        elif self.erros == 4: 
            self.canvas.create_line(120, 90, 150, 110, width=3) 
        elif self.erros == 5: 
            self.canvas.create_line(120, 130, 90, 160, width=3) 
        elif self.erros == 6: 
            self.canvas.create_line(120, 130, 150, 160, width=3) 

    def verificar_letra(self):
        letra = self.entrada.get().upper()
        self.entrada.delete(0, tk.END)

        if not letra or len(letra) > 1 or not letra.isalpha():
            return

        if letra in self.tentativas:
            self.label_status.config(text="Já tentaste essa!", fg="orange")
            return

        self.tentativas.append(letra)

        if letra in self.palavra_secreta:
            for i, l in enumerate(self.palavra_secreta):
                if l == letra:
                    self.letras_acertadas[i] = letra
            self.label_palavra.config(text=" ".join(self.letras_acertadas))
            self.label_status.config(text="Acertaste!", fg="green")
        else:
            self.erros += 1
            self.desenhar_boneco()
            self.label_status.config(text="Erraste!", fg="red")

        self.checar_fim_de_jogo()

    def checar_fim_de_jogo(self):
        if "_" not in self.letras_acertadas:
            messagebox.showinfo("Fim de Jogo", f"Parabéns! Ganhaste.\nA palavra era: {self.palavra_secreta}")
            self.reiniciar_jogo()
        elif self.erros >= 6:
            messagebox.showerror("Fim de Jogo", f"Perbeste!\nA palavra era: {self.palavra_secreta}")
            self.reiniciar_jogo()

if __name__ == "__main__":
    root = tk.Tk()
    app = JogoForcaGUI(root)
    root.mainloop()

import customtkinter as ctk
import subprocess
from random import randint

class FrameMenu(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.app = master

        # Criação e posição do título na janela
        self.label_titulo = ctk.CTkLabel(self, text="Operações Possíveis", font=("arial", 18, "underline", "bold"))
        self.label_titulo.grid(row=0, column=0, pady=(5, 10), padx=10)

        # Criação e posição dos botões
        self.button_100k = ctk.CTkButton(self, text="100.000", command=self.button_100_callback)
        self.button_200k = ctk.CTkButton(self, text="200.000", command=self.button_200_callback)
        self.button_400k = ctk.CTkButton(self, text="400.000", command=self.button_400_callback)
        self.button_800k = ctk.CTkButton(self, text="800.000", command=self.button_800_callback)
        self.button_1_6M = ctk.CTkButton(self, text="1.600.000", command=self.button_16M_callback)

        self.button_100k.grid(row=1, column=0, padx=10, pady=5)
        self.button_200k.grid(row=2, column=0, padx=10, pady=5)
        self.button_400k.grid(row=3, column=0, padx=10, pady=5)
        self.button_800k.grid(row=4, column=0, padx=10, pady=5)
        self.button_1_6M.grid(row=5, column=0, padx=10, pady=5)
    
    # Métodos referentes aos botões
    def button_100_callback(self):
        janela = ctk.CTkInputDialog(text="Quantos testes você deseja realizar com um vetor de 100.000 elementos? (responda com um número inteiro)", title="Testes com 100.000")
        qtd_testes = janela.get_input()
        subprocess.run(["javac", "TesteVetor.java"])
        argumentos = ["100000", str(randint(0, 99999)), qtd_testes]
        with open("Vetor_100K.txt", "w") as arquivo_saida:
            subprocess.run(["java", "TesteVetor"] + argumentos, stdout=arquivo_saida, text=True)

    def button_200_callback(self):
        janela = ctk.CTkInputDialog(text="Quantos testes você deseja realizar com um vetor de 200.000 elementos? (responda com um número inteiro)", title="Testes com 200.000")
        qtd_testes = janela.get_input()
        subprocess.run(["javac", "TesteVetor.java"])
        argumentos = ["200000", str(randint(0, 199999)), qtd_testes]
        with open("Vetor_200K.txt", "w") as arquivo_saida:
            subprocess.run(["java", "TesteVetor"] + argumentos, stdout=arquivo_saida, text=True)

    def button_400_callback(self):
        janela = ctk.CTkInputDialog(text="Quantos testes você deseja realizar com um vetor de 400.000 elementos? (responda com um número inteiro)", title="Testes com 400.000")
        qtd_testes = janela.get_input()
        subprocess.run(["javac", "TesteVetor.java"])
        argumentos = ["400000", str(randint(0, 399999)), qtd_testes]
        with open("Vetor_400K.txt", "w") as arquivo_saida:
            subprocess.run(["java", "TesteVetor"] + argumentos, stdout=arquivo_saida, text=True)

    def button_800_callback(self):
        janela = ctk.CTkInputDialog(text="Quantos testes você deseja realizar com um vetor de 800.000 elementos? (responda com um número inteiro)", title="Testes com 800.000")
        qtd_testes = janela.get_input()
        subprocess.run(["javac", "TesteVetor.java"])
        argumentos = ["800000.txt", str(randint(0, 799999)), qtd_testes]
        with open("Vetor_800K", "w") as arquivo_saida:
            subprocess.run(["java", "TesteVetor"] + argumentos, stdout=arquivo_saida, text=True)

    def button_16M_callback(self):
        janela = ctk.CTkInputDialog(text="Quantos testes você deseja realizar com um vetor de 1.600.000 elementos? (responda com um número inteiro)", title="Testes com 1.600.000")
        qtd_testes = janela.get_input()
        subprocess.run(["javac", "TesteVetor.java"])
        argumentos = ["1600000.txt", str(randint(0, 1599999)), qtd_testes]
        with open("Vetor_1.6M", "w") as arquivo_saida:
            subprocess.run(["java", "TesteVetor"] + argumentos, stdout=arquivo_saida, text=True)

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("300x250")
        self.title("Teste de Perfomance - Algoritmos e Estruturas de Dados")

        # Define o tema do aplicativo a partir do tema padrão do computador
        ctk.set_appearance_mode("system")
        # Frames
        self.frame = FrameMenu(master=self)

        self.frame.pack(side=ctk.TOP, fill=ctk.BOTH, expand=True, padx=0, pady=0)


app = App()
app.mainloop()
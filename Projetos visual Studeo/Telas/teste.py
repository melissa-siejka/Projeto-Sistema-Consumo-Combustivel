
import tkinter as tk
import sqlite3

class CadastroPessoas:
    def __init__(self, root):
        self.root = root

        self.label_nome = tk.Label(root, text="Nome:")
        self.label_nome.grid(row=0, column=0)
        self.entry_nome = tk.Entry(root)
        self.entry_nome.grid(row=0, column=1)

        self.label_idade = tk.Label(root, text="Idade:")
        self.label_idade.grid(row=1, column=0)
        self.entry_idade = tk.Entry(root)
        self.entry_idade.grid(row=1, column=1)

        self.botao_cadastrar = tk.Button(root, text="Cadastrar", command=self.cadastrar_pessoa)
        self.botao_cadastrar.grid(row=2, columnspan=2)

        # Conexão com o banco de dados SQLite
        self.conexao = sqlite3.connect('cadastro_pessoas.db')
        self.criar_tabela()

    def criar_tabela(self):
        cursor = self.conexao.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS pessoas
                          (id INTEGER PRIMARY KEY AUTOINCREMENT,
                          nome TEXT NOT NULL,
                          idade INTEGER NOT NULL)''')
        self.conexao.commit()

    def cadastrar_pessoa(self):
        nome = self.entry_nome.get()
        idade = self.entry_idade.get()

        # Verifica se os campos foram preenchidos
        if nome and idade:
            # Insere os dados no banco de dados
            cursor = self.conexao.cursor()
            cursor.execute("INSERT INTO pessoas (nome, idade) VALUES (?, ?)", (nome, idade))
            self.conexao.commit()
            print("Pessoa cadastrada com sucesso!")
        else:
            print("Por favor, preencha todos os campos.")

root = tk.Tk()
app = CadastroPessoas(root)
root.mainloop()

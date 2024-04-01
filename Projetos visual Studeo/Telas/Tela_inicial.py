# #from tkinter import Tk, Label, Button, Entry, Pack, Place, PhotoImage
# from tkinter import *
# #from Tela_de_cadastro import Tela_cadastro
# import os
# # criando janela inicial
# janela = Tk()
# janela.geometry("800x600")
# janela.title("Tela Inicial")
# janela.configure(bg="#8ab54e")
# janela.iconbitmap("Imagens\icone_coamo.ico")
# img = PhotoImage(file="Imagens\imagemcoamo.png")
# Label(janela, image=img).pack()

# # caminho imagem C:\Users\mayqu\Pictures\Saved Pictures\imagemcoamo
# # Titulo da janela Inicial
# meulabel = Label(janela, text="Seja Bem Vindo Como posso te ajuada?", font=("Arial", 16 ), fg="black", bg="#FFFFFF" )
# meulabel.place(x=300,y=50)

# #botao de cadastro
# botao_cadastra = Button(janela, text="Acessar ", padx=21, bg="#C0C0C0", pady=10,
#                       font=("Arial", 12, "bold"), bd=5, highlightthickness=0)
# botao_cadastra.place(x=100,y=100)


# #botao de consulta
# botao_consultar = Button(janela, text="consulta", bg="#C0C0C0", padx=55, pady=10,
#                          font=("Arial", 12, "bold"), bd=5, highlightthickness=0)
# botao_consultar.place(x=100,y=170)


# #botao de cadstro de informacoes de abastecimeno
# botao_inf_abastecimento = Button(janela, text="inf Abastecimento", bg="#C0C0C0", padx=20, pady=10,
#                                  font=("Arial", 12, "bold"), bd=5, highlightthickness=0)
# botao_inf_abastecimento.place(x=100,y=240)

# # botao Cadastrar rotas
# botao_sair = Button(janela, text="Cadastrar Rotas", bg="#C0C0C0", padx=25, pady=10,
#                     font=("Arial", 12, "bold"), bd=5, highlightthickness=0)
# botao_sair.place(x=100,y=310)


# #botao sair
# botao_sair = Button(janela, text="sair", bg="#C0C0C0", padx=50, pady=10,
#                     font=("Arial", 12, "bold"), bd=5, highlightthickness=0)
# botao_sair.place(x=100,y=380)



# janela.mainloop()

from tkinter import *
import os

Front = Tk()

pastaApp = os.path.dirname(__file__)
Front.iconbitmap("Imagens\icone_coamo.ico")
imgLogo = PhotoImage(file="Imagens\\imagemcoamo.png")
Logo = Label(Front,image=imgLogo)
Logo.place(x=1,y=1)


class Application():
    def __init__(self):
        self.Front = Front
        self.tela()
        #self.frameTela()
        self.BotaoTela()
        Front.mainloop()

    def tela(self):
        self.Front.title("Sistema Consumo de Combustível")  # Define o nome da janela do programa
        self.Front.geometry("1070x665")  # Define o tamanho da tela
        self.Front.resizable(False, False)  # Confirma se a tela pode ou não ser responsiva (aumentar ou diminuir de tamanho)

    def BotaoTela(self):

    # Tela Cadastro de Veículos
        self.Limpar = Button(self.Front,text='Cadastro de Veículos', bg='#D6FADC',font=('Segoe UI Semibold', 11), fg='black')
        self.Limpar.place(relx=0.10, rely=0.30, relwidth=0.30, relheight=0.05)
    # Tela Cadastro Posto Conveniado
        self.Limpar = Button(self.Front,text='Cadastro de Postos Conveniados', bg='#D6FADC',font=('Segoe UI Semibold', 11), fg='black')
        self.Limpar.place(relx=0.10, rely=0.45, relwidth=0.30, relheight=0.05)
    # Tela Registro de Abastecimento
        self.Limpar = Button(self.Front,text='Registro de Abastecimento', bg='#D6FADC',font=('Segoe UI Semibold', 11), fg='black')
        self.Limpar.place(relx=0.10, rely=0.60, relwidth=0.30, relheight=0.05)
    # Tela Relatório Consumo de Combustível
        self.Limpar = Button(self.Front,text='Relatório Consumo de Combustível', bg='#D6FADC',font=('Segoe UI Semibold', 11), fg='black')
        self.Limpar.place(relx=0.10, rely=0.75, relwidth=0.30, relheight=0.05)
    # Criação da Label e Entrada de Código

nova = Application()
nova.tela
nova.BotaoTela
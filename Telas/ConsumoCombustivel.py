from tkinter import *
import os

TelaCadastroVeiculo = Tk()

pastaApp = os.path.dirname(__file__)
imgLogo = PhotoImage(file=pastaApp+"\\Imagens\RelatorioCombustivel.png")
Logo = Label(TelaCadastroVeiculo, image=imgLogo)
Logo.place(x=10,y=10)

class Application2():
    def __init__(self):
        self.TelaCadastroVeiculo = TelaCadastroVeiculo
        self.tela()
      #  self.frameTela()
        self.BotaoTela()
        TelaCadastroVeiculo.mainloop()

    def tela(self):
        self.TelaCadastroVeiculo.title("Sistema Consumo de Combustível")  # Define o nome da janela do programa
        self.TelaCadastroVeiculo.geometry("1070x665") # Define o tamanho da tela
        self.TelaCadastroVeiculo.resizable(False, False)  # Confirma se a tela pode ou não ser responsiva (aumentar ou diminuir de tamanho)

    def BotaoTela(self):
    # Botão Limpar
        self.Limpar = Button(self.TelaCadastroVeiculo, text='Limpar',bg='#D6FADC',font=('Arial', 9), fg='black')
        self.Limpar.place(relx=0.80, rely=0.09, relwidth=0.1, relheight=0.05)
        # Botão Buscar
        self.Buscar = Button(self.TelaCadastroVeiculo, text='Buscar',bg='#D6FADC',font=('Arial', 9), fg='black')  # Indica em qual frame estará o botão, com o texto informando a sua função
        self.Buscar.place(relx=0.70, rely=0.09, relwidth=0.1, relheight=0.05)
        # Botão Novo Registro
        self.Novo = Button(self.TelaCadastroVeiculo, text='Inserir novo registro',bg='#D6FADC',font=('Arial', 9), fg='black')  # Indica em qual frame estará o botão, com o texto informando a sua função
        self.Novo.place(relx=0.57, rely=0.09, relwidth=0.13, relheight=0.05)

    # Criação da label de entrada do código
        # Id Veículo
        self.lb_IdVeiculo = Label(self.TelaCadastroVeiculo, text='Id Veículo')
        self.lb_IdVeiculo.place(relx=0.11, rely=0.24, relwidth=0.15, relheight=0.04)
        self.IdVeiculo_entry = Entry(self.TelaCadastroVeiculo, font=('Segoe UI Semibold',9))
        self.IdVeiculo_entry.place(relx=0.11, rely=0.28, relwidth=0.15, relheight=0.06)  # Entrada do registro
        # Placa
        self.lb_Placa= Label(self.TelaCadastroVeiculo, text='Placa')
        self.lb_Placa.place(relx=0.30, rely=0.24, relwidth=0.15, relheight=0.04)
        self.Placa_entry = Entry(self.TelaCadastroVeiculo, font=('Segoe UI Semibold',9))
        self.Placa_entry.place(relx=0.30, rely=0.28, relwidth=0.15, relheight=0.06)  # Entrada do registro
        # Tipo de Veículo
        self.lb_TipoVeiculo= Label(self.TelaCadastroVeiculo, text='Tipo de Veículo')
        self.lb_TipoVeiculo.place(relx=0.51, rely=0.24, relwidth=0.15, relheight=0.04)
        self.TipoVeiculo_entry = Entry(self.TelaCadastroVeiculo, font=('Segoe UI Semibold',9))
        self.TipoVeiculo_entry.place(relx=0.51, rely=0.28, relwidth=0.15, relheight=0.06)  # Entrada do registro
        # Tipo de combustível
        self.lb_TipoCombustivel = Label(self.TelaCadastroVeiculo, text='Tipo de Combustível')
        self.lb_TipoCombustivel.place(relx=0.70, rely=0.24, relwidth=0.15, relheight=0.04)
        self.TipoCombustivel_entry = Entry(self.TelaCadastroVeiculo, font=('Segoe UI Semibold',9))
        self.TipoCombustivel_entry.place(relx=0.70, rely=0.28, relwidth=0.15, relheight=0.06)  # Entrada do registro
        # Ativo

        # Capacidade de Tanque

        # Data aquisição

        # Data Baixa

Application2()

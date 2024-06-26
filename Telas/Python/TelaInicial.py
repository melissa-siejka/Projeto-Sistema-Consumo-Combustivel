from tkinter import *
import os
#from TelaCadastroVeiculo import Application as CadastroVeiculo

TelaInicial = Tk()

pastaApp = os.path.dirname(__file__)
imgLogo = PhotoImage(file=pastaApp+"\\Imagens\Tela Inicial.png")
Logo = Label(TelaInicial, image=imgLogo)
Logo.place(x=1, y=1)

class Application():
    def __init__(self):
        self.Front = TelaInicial
        self.tela()
        self.BotaoTela()
        TelaInicial.mainloop()

    def tela(self):
        self.Front.title("Sistema Consumo de Combustível")  # Define o nome da janela do programa
        self.Front.geometry("1070x665")  # Define o tamanho da tela
        self.Front.resizable(False, False)  # Confirma se a tela pode ou não ser responsiva (aumentar ou diminuir de tamanho)



    def BotaoTela(self):
        # Tela Cadastro de Veículos
        self.CadVeiculo = Button(self.Front, text='Cadastro de Veículos', bg='#D6FADC', font=('Segoe UI Semibold', 11), fg='black')
        self.CadVeiculo.place(relx=0.17, rely=0.22, relwidth=0.30, relheight=0.05)
        # Tela Cadastro Posto Conveniado
        self.CadPosto = Button(self.Front, text='Cadastro de Postos Conveniados', bg='#D6FADC', font=('Segoe UI Semibold', 11), fg='black')
        self.CadPosto.place(relx=0.17, rely=0.42, relwidth=0.30, relheight=0.05)
        # Tela Registro de Abastecimento
        self.Abastecimento = Button(self.Front, text='Registro de Abastecimento', bg='#D6FADC', font=('Segoe UI Semibold', 11), fg='black')
        self.Abastecimento.place(relx=0.17, rely=0.62, relwidth=0.30, relheight=0.05)
        # Tela Relatório Consumo de Combustível
        self.RelatorioComb = Button(self.Front, text='Relatório Consumo de Combustível', bg='#D6FADC', font=('Segoe UI Semibold', 11), fg='black')
        self.RelatorioComb.place(relx=0.17, rely=0.82, relwidth=0.30, relheight=0.05)

Application()

from tkinter import *
import os
import sqlite3

TelaCadastroPosto = Tk()

pastaApp = os.path.dirname(__file__)
imgLogo = PhotoImage(file=pastaApp+"\\Imagens\PostoConveniado.png")
Logo = Label(TelaCadastroPosto, image=imgLogo)
Logo.place(x=10,y=10)

# Função limpa entrada da tela
class FuncaoTela ():
    def limpaTela(self):
        self.CodPosto_entry.delete(0, END)
        self.NomePosto_entry.delete(0, END)
        self.DtConvenio_entry.delete(0, END)
        self.DtDesconvenio_entry.delete(0, END)

# Inserir função CadPosto


# Classe tela inicial
class Application2(FuncaoTela):
    def __init__(self):
        self.TelaCadastroVeiculo = TelaCadastroPosto
        self.tela()
        self.BotaoTela()
        TelaCadastroPosto.mainloop()
# Função de configuração do layout da tela
    def tela(self):
        self.TelaCadastroVeiculo.title("Sistema Consumo de Combustível")  # Define o nome da janela do programa
        self.TelaCadastroVeiculo.geometry("1070x665") # Define o tamanho da tela
        self.TelaCadastroVeiculo.resizable(False, False)  # Confirma se a tela pode ou não ser responsiva (aumentar ou diminuir de tamanho)

# Função de criação dos botões da tela de cadastro
    def BotaoTela(self):
    # Botão Limpar
        self.Limpar = Button(self.TelaCadastroVeiculo, text='Limpar',bg='#D6FADC',font=('Arial', 9), fg='black', command=self.limpaTela)
        self.Limpar.place(relx=0.80, rely=0.78, relwidth=0.1, relheight=0.05)
        # Botão Novo Registro
        self.Novo = Button(self.TelaCadastroVeiculo, text='Inserir novo registro',bg='#D6FADC',font=('Arial', 9), fg='black')  #
        self.Novo.place(relx=0.11, rely=0.78, relwidth=0.13, relheight=0.05)

    # Criação da label de entrada do código
        # Código Posto
        self.lb_CodPosto = Label(self.TelaCadastroVeiculo, text='Código Posto',font=('Segoe UI Semibold', 10),bg = '#00602C',fg='white')
        self.lb_CodPosto.place(relx=0.11, rely=0.34, relwidth=0.15, relheight=0.04)
        self.CodPosto_entry = Entry(self.TelaCadastroVeiculo, font=('Segoe UI Semibold',9), highlightthickness=1, highlightbackground='#BFBFBF')
        self.CodPosto_entry.place(relx=0.11, rely=0.38, relwidth=0.15, relheight=0.06)  # Entrada do registro
        # Nome Posto
        self.lb_NomePosto= Label(self.TelaCadastroVeiculo,bg = '#00602C',fg='white', text='POSTO CONVENIADO',font=('Segoe UI Semibold', 10), )
        self.lb_NomePosto.place(relx=0.30, rely=0.34, relwidth=0.15, relheight=0.04)
        self.NomePosto_entry = Entry(self.TelaCadastroVeiculo, font=('Segoe UI Semibold',9), highlightthickness=1, highlightbackground='#BFBFBF')
        self.NomePosto_entry.place(relx=0.30, rely=0.38, relwidth=0.15, relheight=0.05)
        # Data Convenio
        self.lb_DtConvenio= Label(self.TelaCadastroVeiculo, text='DATA CONVÊNIO',font=('Segoe UI Semibold', 10),bg = '#00602C',fg='white')
        self.lb_DtConvenio.place(relx=0.51, rely=0.34, relwidth=0.15, relheight=0.04)
        self.DtConvenio_entry = Entry(self.TelaCadastroVeiculo, font=('Segoe UI Semibold',9), highlightthickness=1, highlightbackground='#BFBFBF')
        self.DtConvenio_entry.place(relx=0.51, rely=0.38, relwidth=0.15, relheight=0.05)
        # Data Desconvenio
        self.lb_DtDesconvenio = Label(self.TelaCadastroVeiculo, text='DATA DESCONVENIO',font=('Segoe UI Semibold', 10), bg = '#00602C',fg='white')
        self.lb_DtDesconvenio.place(relx=0.70, rely=0.34, relwidth=0.15, relheight=0.04)
        self.DtDesconvenio_entry = Entry(self.TelaCadastroVeiculo, font=('Segoe UI Semibold',9), highlightthickness=1, highlightbackground='#BFBFBF')
        self.DtDesconvenio_entry.place(relx=0.70, rely=0.38, relwidth=0.15, relheight=0.05)



Application2()

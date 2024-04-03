from tkinter import *
import os

TelaAbastecimento = Tk()

pastaApp = os.path.dirname(__file__)
imgLogo = PhotoImage(file=pastaApp+"\\Imagens\Abastecimento.png")
Logo = Label(TelaAbastecimento, image=imgLogo)
Logo.place(x=10,y=10)

# Função limpa entrada da tela
class FuncaoTela ():
    def limpaTela(self):
        self.Requisicao_entry.delete(0, END)
        self.IdVeiculo_entry.delete(0, END)
        self.Motorista_entry.delete(0, END)
        self.TipoCombustivel_entry.delete(0, END)
        self.DtAbastecimento_entry.delete(0, END)
        self.Hodometro_entry.delete(0, END)
        self.Litro_entry.delete(0, END)
        self.VlComb_entry.delete(0, END)

# Inserir função CadAbastecimento

# Classe tela inicial
class Application(FuncaoTela):
    def __init__(self):
        self.TelaAbastecimento = TelaAbastecimento
        self.tela()
        self.BotaoTela()
        TelaAbastecimento.mainloop()
# Função de configuração do layout da tela
    def tela(self):
        self.TelaAbastecimento.title("Sistema Consumo de Combustível")  # Define o nome da janela do programa
        self.TelaAbastecimento.geometry("1070x665") # Define o tamanho da tela
        self.TelaAbastecimento.resizable(False, False)  # Confirma se a tela pode ou não ser responsiva (aumentar ou diminuir de tamanho)

# Função de criação dos botões da tela de cadastro
    def BotaoTela(self):
    # Botão Limpar
        self.Limpar = Button(self.TelaAbastecimento, text='Limpar',bg='#D6FADC',font=('Arial', 9), fg='black', command=self.limpaTela)
        self.Limpar.place(relx=0.80, rely=0.78, relwidth=0.1, relheight=0.05)
        # Botão Novo Registro
        self.Novo = Button(self.TelaAbastecimento, text='Inserir novo registro',bg='#D6FADC',font=('Arial', 9), fg='black')  # Indica em qual frame estará o botão, com o texto informando a sua função
        self.Novo.place(relx=0.11, rely=0.78, relwidth=0.13, relheight=0.05)

    # Criação da label de entrada do código
        # Nr Requisicao
        self.lb_Requisicao = Label(self.TelaAbastecimento, text='Nº REQUISIÇÃO',font=('Segoe UI Semibold', 10),bg = '#00602C',fg='white')
        self.lb_Requisicao.place(relx=0.11, rely=0.24, relwidth=0.15, relheight=0.04)
        self.Requisicao_entry = Entry(self.TelaAbastecimento, font=('Segoe UI Semibold',9), highlightthickness=1, highlightbackground='#BFBFBF')
        self.Requisicao_entry.place(relx=0.11, rely=0.28, relwidth=0.15, relheight=0.06)  # Entrada do registro
        # Id Veículo
        self.lb_IdVeiculo= Label(self.TelaAbastecimento,bg = '#00602C',fg='white', text='VEÍCULO',font=('Segoe UI Semibold', 10), )
        self.lb_IdVeiculo.place(relx=0.30, rely=0.24, relwidth=0.15, relheight=0.04)
        self.IdVeiculo_entry = Entry(self.TelaAbastecimento, font=('Segoe UI Semibold',9), highlightthickness=1, highlightbackground='#BFBFBF')
        self.IdVeiculo_entry.place(relx=0.30, rely=0.28, relwidth=0.15, relheight=0.05)
        # Motorista
        self.lb_Motorista= Label(self.TelaAbastecimento, text='MOTORISTA',font=('Segoe UI Semibold', 10),bg = '#00602C',fg='white')
        self.lb_Motorista.place(relx=0.51, rely=0.24, relwidth=0.15, relheight=0.04)
        self.Motorista_entry = Entry(self.TelaAbastecimento, font=('Segoe UI Semibold',9), highlightthickness=1, highlightbackground='#BFBFBF')
        self.Motorista_entry.place(relx=0.51, rely=0.28, relwidth=0.15, relheight=0.05)
        # Tipo de combustível
        self.lb_TipoCombustivel = Label(self.TelaAbastecimento, text='TIPO DE COMBUSTÍVEL',font=('Segoe UI Semibold', 10), bg = '#00602C',fg='white')
        self.lb_TipoCombustivel.place(relx=0.70, rely=0.24, relwidth=0.15, relheight=0.04)
        self.Tipvar = StringVar(self.TelaAbastecimento)
        self.TipV = ("Diesel S10", "Diesel S500","Etanol","Gasolina","GLP")
        self.Tipvar.set('Diesel S10')
        self.popupMenu = OptionMenu (self.TelaAbastecimento, self.Tipvar, *self.TipV)
        self.popupMenu.place(relx=0.70, rely=0.28, relwidth=0.15, relheight=0.05)

        # Data abastecimento
        self.lb_DtAbastecimento= Label(self.TelaAbastecimento, text='DATA ABASTECIMENTO',font=('Segoe UI Semibold', 10),bg = '#00602C',fg='white')
        self.lb_DtAbastecimento.place(relx=0.11, rely=0.44, relwidth=0.15, relheight=0.04)
        self.DtAbastecimento_entry = Entry(self.TelaAbastecimento, font=('Segoe UI Semibold',9), highlightthickness=1, highlightbackground='#BFBFBF')
        self.DtAbastecimento_entry.place(relx=0.11, rely=0.48, relwidth=0.15, relheight=0.05)

        # Hodômetro
        self.lb_Hodometro = Label(self.TelaAbastecimento, text='HODÔMETRO',font=('Segoe UI Semibold', 10),bg = '#00602C',fg='white')
        self.lb_Hodometro.place(relx=0.30, rely=0.44, relwidth=0.15, relheight=0.04)
        self.Hodometro_entry = Entry(self.TelaAbastecimento, font=('Segoe UI Semibold',9), highlightthickness=1, highlightbackground='#BFBFBF')
        self.Hodometro_entry.place(relx=0.30, rely=0.48, relwidth=0.15, relheight=0.05)

        # Litros
        self.lb_Litro = Label(self.TelaAbastecimento, text='LITROS',font=('Segoe UI Semibold', 10),bg = '#00602C',fg='white')
        self.lb_Litro.place(relx=0.51, rely=0.44, relwidth=0.15, relheight=0.04)
        self.Litro_entry = Entry(self.TelaAbastecimento, font=('Segoe UI Semibold',9), highlightthickness=1, highlightbackground='#BFBFBF')
        self.Litro_entry.place(relx=0.51, rely=0.48, relwidth=0.15, relheight=0.05)

        # Valor
        self.lb_VlComb= Label(self.TelaAbastecimento, text='VALOR COMBUSTIVEL',font=('Segoe UI Semibold', 10),bg = '#00602C',fg='white')
        self.lb_VlComb.place(relx=0.71, rely=0.44, relwidth=0.15, relheight=0.04)
        self.VlComb_entry = Entry(self.TelaAbastecimento, font=('Segoe UI Semibold',9), highlightthickness=1, highlightbackground='#BFBFBF')
        self.VlComb_entry.place(relx=0.71, rely=0.48, relwidth=0.15, relheight=0.05)



Application()

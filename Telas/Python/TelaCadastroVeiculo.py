from tkinter import *
import os

TelaCadastroVeiculo = Tk()

pastaApp = os.path.dirname(__file__)
imgLogo = PhotoImage(file=pastaApp+"\\Imagens\CadastroVeiculo.png")
Logo = Label(TelaCadastroVeiculo, image=imgLogo)
Logo.place(x=10,y=10)

# Função limpa entrada da tela
class FuncaoTela ():
    def limpaTela(self):
        self.IdVeiculo_entry.delete(0, END)
        self.Placa_entry.delete(0, END)
        self.TipoVeiculo_entry.delete(0, END)
        self.TipoCombustivel_entry.delete(0, END)
        self.DtAquisicao_entry.delete(0, END)
        self.DtBaixa_entry.delete(0, END)

# Inserir função CadVeiculo

# Classe tela inicial
class Application(FuncaoTela):
    def __init__(self):
        self.TelaCadastroVeiculo = TelaCadastroVeiculo
        self.tela()
        self.BotaoTela()
        TelaCadastroVeiculo.mainloop()
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
        # Botão Buscar
        self.Buscar = Button(self.TelaCadastroVeiculo, text='Buscar',bg='#FCB546',font=('Arial', 9), fg='black')  # Indica em qual frame estará o botão, com o texto informando a sua função
        self.Buscar.place(relx=0.80, rely=0.11, relwidth=0.1, relheight=0.05)
        # Botão Novo Registro
        self.Novo = Button(self.TelaCadastroVeiculo, text='Inserir novo registro',bg='#D6FADC',font=('Arial', 9), fg='black')  # Indica em qual frame estará o botão, com o texto informando a sua função
        self.Novo.place(relx=0.11, rely=0.78, relwidth=0.13, relheight=0.05)

    # Criação da label de entrada do código
        # Id Veículo
        self.lb_IdVeiculo = Label(self.TelaCadastroVeiculo, text='ID VEÍCULO',font=('Segoe UI Semibold', 10),bg = '#00602C',fg='white')
        self.lb_IdVeiculo.place(relx=0.11, rely=0.24, relwidth=0.15, relheight=0.04)
        self.IdVeiculo_entry = Entry(self.TelaCadastroVeiculo, font=('Segoe UI Semibold',9), highlightthickness=1, highlightbackground='#BFBFBF')
        self.IdVeiculo_entry.place(relx=0.11, rely=0.28, relwidth=0.15, relheight=0.06)  # Entrada do registro
        # Placa
        self.lb_Placa= Label(self.TelaCadastroVeiculo,bg = '#00602C',fg='white', text='PLACA',font=('Segoe UI Semibold', 10), )
        self.lb_Placa.place(relx=0.30, rely=0.24, relwidth=0.15, relheight=0.04)
        self.Placa_entry = Entry(self.TelaCadastroVeiculo, font=('Segoe UI Semibold',9), highlightthickness=1, highlightbackground='#BFBFBF')
        self.Placa_entry.place(relx=0.30, rely=0.28, relwidth=0.15, relheight=0.05)
        # Tipo de Veículo
        self.lb_TipoVeiculo= Label(self.TelaCadastroVeiculo, text='TIPO DE VEÍCULO',font=('Segoe UI Semibold', 10),bg = '#00602C',fg='white')
        self.lb_TipoVeiculo.place(relx=0.51, rely=0.24, relwidth=0.15, relheight=0.04)
        self.TipoVeiculo_entry = Entry(self.TelaCadastroVeiculo, font=('Segoe UI Semibold',9), highlightthickness=1, highlightbackground='#BFBFBF')
        self.TipoVeiculo_entry.place(relx=0.51, rely=0.28, relwidth=0.15, relheight=0.05)
        # Tipo de combustível
        self.lb_TipoCombustivel = Label(self.TelaCadastroVeiculo, text='TIPO DE COMBUSTÍVEL',font=('Segoe UI Semibold', 10), bg = '#00602C',fg='white')
        self.lb_TipoCombustivel.place(relx=0.70, rely=0.24, relwidth=0.15, relheight=0.04)
        self.TipoCombustivel_entry = Entry(self.TelaCadastroVeiculo, font=('Segoe UI Semibold',9), highlightthickness=1, highlightbackground='#BFBFBF')
        self.TipoCombustivel_entry.place(relx=0.70, rely=0.28, relwidth=0.15, relheight=0.05)
        # Capacidade de Tanque
        self.lb_Tanque = Label(self.TelaCadastroVeiculo, text='CAPACIDADE DE TANQUE',font=('Segoe UI Semibold', 10),bg = '#00602C',fg='white')
        self.lb_Tanque.place(relx=0.11, rely=0.44, relwidth=0.15, relheight=0.04)
        self.Tanque_entry = Entry(self.TelaCadastroVeiculo, font=('Segoe UI Semibold',9), highlightthickness=1, highlightbackground='#BFBFBF')
        self.Tanque_entry.place(relx=0.11, rely=0.48, relwidth=0.15, relheight=0.05)

        # Data aquisição
        self.lb_DtAquisicao = Label(self.TelaCadastroVeiculo, text='DATA DE AQUISICAO',font=('Segoe UI Semibold', 10),bg = '#00602C',fg='white')
        self.lb_DtAquisicao.place(relx=0.30, rely=0.44, relwidth=0.15, relheight=0.04)
        self.DtAquisicao_entry = Entry(self.TelaCadastroVeiculo, font=('Segoe UI Semibold',9), highlightthickness=1, highlightbackground='#BFBFBF')
        self.DtAquisicao_entry.place(relx=0.30, rely=0.48, relwidth=0.15, relheight=0.05)
        # Data Baixa
        self.lb_DtBaixa= Label(self.TelaCadastroVeiculo, text='DATA DE BAIXA',font=('Segoe UI Semibold', 10),bg = '#00602C',fg='white')
        self.lb_DtBaixa.place(relx=0.51, rely=0.44, relwidth=0.15, relheight=0.04)
        self.DtBaixa_entry = Entry(self.TelaCadastroVeiculo, font=('Segoe UI Semibold',9), highlightthickness=1, highlightbackground='#BFBFBF')
        self.DtBaixa_entry.place(relx=0.51, rely=0.48, relwidth=0.15, relheight=0.05)
        # Indicado ativo



Application()

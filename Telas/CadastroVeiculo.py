from tkinter import *
import os
import sqlite3

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
#Define conexão com banco de dados (alterar para conexão Sistema Consumo de Combustível)
    def conectaBd(self):
        self.conn = sqlite3.connect("clientes.bd")
        self.cursor = self.conn.cursor()
#Define desconexão com o banco de dados
    def desconetaBd(self):
        self.conn.close();print("Desconectando ao banco de dados")
# Criação da tabela (no projeto, deve ser alterado para a conexão com a tabela no Oracle SQL
    def montaTabela (self):
        self.conectaBd();print("Conectando ao banco de dados")
        ### Criar tabela
        self.cursor.execute("""
             CREATE TABLE IF NOT EXISTS veiculo (
                id_veiculo   NUMBER(7) NOT NULL,
                nr_placa     CHAR(7) NOT NULL,
                dt_aquisicao        DATE NOT NULL,
                dt_baixa            DATE,
                qt_capacidadetanque INTEGER NOT NULL,
                in_ativo            CHAR(1) NOT NULL,
                cd_tipoveiculo      NUMBER(3) NOT NULL,
                cd_tipocombustivel  NUMBER(3) NOT NULL
             );
        """)
        self.conn.commit();print("Banco de dados criado")
        self.desconetaBd()
# Inserção de veículo no banco
    def addVeiculo (self):
        self.IdVeiculo = self.IdVeiculo_entry.get()
        self.Placa = self.Placa_entry.get()
        self.DtAquisicao = self.DtAquisicao.get()
        self.DtBaixa = self.DtBaixa.get()
        self.CapacidadeTanque = self.CapacidadeTanque.get()
        self.Ativo = self.Ativo.get()
        self.TpVeiculo = self.TpVeiculo.get()
        self.TpComb = self.TpComb.get()

        self.conectaBd()

        self.cursor.execute("""" INSERT INTO VEICULO (id_veiculo, nr_placa, dt_aquisicao, dt_baixa, qt_capacidadetanque, in_ativo, cd_tipoveiculo, cd_tipocombustivel)
        VALUES(1001,'ABC9J10', '10/05/2019', null, 360, 'T',3,3);""",(self.IdVeiculo, self.Placa, self.DtAquisicao, self.DtBaixa,self.CapacidadeTanque, self.Ativo, self.TpVeiculo, self.TpComb))
        self.conn.commit()
        self.desconetaBd()

####   def selectLista (self):
    ##    self.ListaVeiculo.delete(*self.ListaVeiculo.get_childen())
      #  self.conectaBd()
       #lista = self.cursor.execute(""" SELECT """) """""""


# Classe tela inicial
class Application2(FuncaoTela):
    def __init__(self):
        self.TelaCadastroVeiculo = TelaCadastroVeiculo
        self.tela()
        self.BotaoTela()
        self.montaTabela() ## adaptar para banco de dados Sistema Combustivel
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



Application2()

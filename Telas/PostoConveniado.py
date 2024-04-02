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
        self.TelaCadastroVeiculo = TelaCadastroPosto
        self.tela()
        self.BotaoTela()
        self.montaTabela() ## adaptar para banco de dados Sistema Combustivel
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
        # Botão Buscar
        self.Buscar = Button(self.TelaCadastroVeiculo, text='Buscar',bg='#FCB546',font=('Arial', 9), fg='black')  # Indica em qual frame estará o botão, com o texto informando a sua função
        self.Buscar.place(relx=0.80, rely=0.11, relwidth=0.1, relheight=0.05)
        # Botão Novo Registro
        self.Novo = Button(self.TelaCadastroVeiculo, text='Inserir novo registro',bg='#D6FADC',font=('Arial', 9), fg='black')  # Indica em qual frame estará o botão, com o texto informando a sua função
        self.Novo.place(relx=0.11, rely=0.78, relwidth=0.13, relheight=0.05)

    # Criação da label de entrada do código
        # Código Posto
        self.lb_CodPosto = Label(self.TelaCadastroVeiculo, text='Código Posto',font=('Segoe UI Semibold', 10),bg = '#00602C',fg='white')
        self.lb_CodPosto.place(relx=0.11, rely=0.24, relwidth=0.15, relheight=0.04)
        self.CodPosto_entry = Entry(self.TelaCadastroVeiculo, font=('Segoe UI Semibold',9), highlightthickness=1, highlightbackground='#BFBFBF')
        self.CodPosto_entry.place(relx=0.11, rely=0.28, relwidth=0.15, relheight=0.06)  # Entrada do registro
        # Nome Posto
        self.lb_NomePosto= Label(self.TelaCadastroVeiculo,bg = '#00602C',fg='white', text='POSTO CONVENIADO',font=('Segoe UI Semibold', 10), )
        self.lb_NomePosto.place(relx=0.30, rely=0.24, relwidth=0.15, relheight=0.04)
        self.NomePosto_entry = Entry(self.TelaCadastroVeiculo, font=('Segoe UI Semibold',9), highlightthickness=1, highlightbackground='#BFBFBF')
        self.NomePosto_entry.place(relx=0.30, rely=0.28, relwidth=0.15, relheight=0.05)
        # Data Convenio
        self.lb_DtConvenio= Label(self.TelaCadastroVeiculo, text='DATA CONVÊNIO',font=('Segoe UI Semibold', 10),bg = '#00602C',fg='white')
        self.lb_DtConvenio.place(relx=0.51, rely=0.24, relwidth=0.15, relheight=0.04)
        self.DtConvenio_entry = Entry(self.TelaCadastroVeiculo, font=('Segoe UI Semibold',9), highlightthickness=1, highlightbackground='#BFBFBF')
        self.DtConvenio_entry.place(relx=0.51, rely=0.28, relwidth=0.15, relheight=0.05)
        # Data Desconvenio
        self.lb_DtDesconvenio = Label(self.TelaCadastroVeiculo, text='DATA DESCONVENIO',font=('Segoe UI Semibold', 10), bg = '#00602C',fg='white')
        self.lb_DtDesconvenio.place(relx=0.70, rely=0.24, relwidth=0.15, relheight=0.04)
        self.DtDesconvenio_entry = Entry(self.TelaCadastroVeiculo, font=('Segoe UI Semibold',9), highlightthickness=1, highlightbackground='#BFBFBF')
        self.DtDesconvenio_entry.place(relx=0.70, rely=0.28, relwidth=0.15, relheight=0.05)



Application2()

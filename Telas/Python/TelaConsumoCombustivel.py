from tkinter import *
from tkinter import ttk
import os

TelaRelatorio = Tk()

pastaApp = os.path.dirname(__file__)
imgLogo = PhotoImage(file=pastaApp+"\\Imagens\RelatorioConsumo.png")
Logo = Label(TelaRelatorio, image=imgLogo)
Logo.place(x=10,y=10)

# Função limpa entrada da tela
class FuncaoTela ():
    def limpaTela(self):
        self.DtInicial_entry.delete(0, END)
        self.DtFim_entry.delete(0, END)
        self.Unidade_entry.delete(0, END)
        self.TpVeiculo_entry.delete(0, END)
        self.DtAquisicao_entry.delete(0, END)
        self.IdVeiculo_entry.delete(0, END)

# Inserir função CadAbastecimento

# Classe tela inicial
class Application(FuncaoTela):
    def __init__(self):
        self.TelaRelatorio = TelaRelatorio
        self.tela()
        self.frameTela()
        self.BotaoTela()
        self.ResultadoPesquisa()
        TelaRelatorio.mainloop()


# Função de configuração do layout da tela
    def tela(self):
        self.TelaRelatorio.title("Sistema Consumo de Combustível")  # Define o nome da janela do programa
        self.TelaRelatorio.geometry("1070x665") # Define o tamanho da tela
        self.TelaRelatorio.resizable(False, False)  # Confirma se a tela pode ou não ser responsiva (aumentar ou diminuir de tamanho)

    def frameTela (self):
        self.frameResultado = Frame(self.TelaRelatorio, bg = 'white',highlightthickness=3, highlightbackground='#BFBFBF')
        self.frameResultado.place (relx=0.05, rely = 0.35, relwidth=0.9, relheight=0.5)

# Função de criação dos botões da tela de cadastro
    def BotaoTela(self):
    # Botão Limpar
        self.Limpar = Button(self.TelaRelatorio, text='Limpar', bg='#D6FADC', font=('Arial', 9), fg='black', command=self.limpaTela)
        self.Limpar.place(relx=0.80, rely=0.88, relwidth=0.1, relheight=0.05)
        # Botão Buscar
        self.Buscar = Button(self.TelaRelatorio, text='Buscar', bg='#FCB546', font=('Arial', 9), fg='black')  # Indica em qual frame estará o botão, com o texto informando a sua função
        self.Buscar.place(relx=0.80, rely=0.11, relwidth=0.1, relheight=0.05)
        # Botão Novo Registro
        self.ExportarExcel = Button(self.TelaRelatorio, text='Exportar para Excel', bg='#D6FADC', font=('Arial', 9), fg='black')  # Indica em qual frame estará o botão, com o texto informando a sua função
        self.ExportarExcel.place(relx=0.11, rely=0.88, relwidth=0.13, relheight=0.05)

    # Criação da label de entrada do código

        # Data Inicial
        self.lb_DtInicial= Label(self.TelaRelatorio, text='Data Inicial', font=('Segoe UI Semibold', 10), bg ='#D6FADC', fg='black')
        self.lb_DtInicial.place(relx=0.09, rely=0.20, relwidth=0.15, relheight=0.03)
        self.DtInicial_entry = Entry(self.TelaRelatorio, font=('Segoe UI Semibold', 9), highlightthickness=1, highlightbackground='#BFBFBF')
        self.DtInicial_entry.place(relx=0.09, rely=0.23 ,relwidth=0.15, relheight=0.05)

        # Data Fim
        self.lb_DtFim= Label(self.TelaRelatorio, text='Data Final', font=('Segoe UI Semibold', 10), bg ='#D6FADC', fg='black')
        self.lb_DtFim.place(relx=0.25, rely=0.20, relwidth=0.15, relheight=0.03)
        self.DtFim_entry = Entry(self.TelaRelatorio, font=('Segoe UI Semibold', 9), highlightthickness=1, highlightbackground='#BFBFBF')
        self.DtFim_entry.place(relx=0.25, rely=0.23 ,relwidth=0.15, relheight=0.05)

        # Unidade Veículo
        self.lb_Unidade= Label(self.TelaRelatorio, text='Unidade', font=('Segoe UI Semibold', 10), bg ='#D6FADC', fg='black')
        self.lb_Unidade.place(relx=0.41, rely=0.20, relwidth=0.15, relheight=0.03)
        self.Unidade_entry = Entry(self.TelaRelatorio, font=('Segoe UI Semibold', 9), highlightthickness=1, highlightbackground='#BFBFBF')
        self.Unidade_entry.place(relx=0.41, rely=0.23 ,relwidth=0.15, relheight=0.05)

        # Tipo de Veículo
        self.lb_TpVeiculo= Label(self.TelaRelatorio, text='Tipo de Veículo', font=('Segoe UI Semibold', 10), bg ='#D6FADC', fg='black')
        self.lb_TpVeiculo.place(relx=0.57, rely=0.20, relwidth=0.15, relheight=0.03)
        self.Tipvar = StringVar(self.TelaRelatorio)
        self.TipV = ("Leve", "Médio","Pesado")
        self.Tipvar.set('Leve')
        self.popupMenu = OptionMenu (self.TelaRelatorio, self.Tipvar, *self.TipV)
        self.popupMenu.place(relx=0.57, rely=0.23 ,relwidth=0.15, relheight=0.05)

        # Veículo
        self.lb_IdVeiculo= Label(self.TelaRelatorio, text='Id Veículo', font=('Segoe UI Semibold', 10), bg ='#D6FADC', fg='black')
        self.lb_IdVeiculo.place(relx=0.73, rely=0.20, relwidth=0.15, relheight=0.03)
        self.IdVeiculo_entry = Entry(self.TelaRelatorio, font=('Segoe UI Semibold', 9), highlightthickness=1, highlightbackground='#BFBFBF')
        self.IdVeiculo_entry.place(relx=0.73, rely=0.23 ,relwidth=0.15, relheight=0.05)

        #Lista de resultado

    def ResultadoPesquisa (self):
        self.ConsumoComb = ttk.Treeview(self.frameResultado, height= 3, column = ('col1', 'col2', 'col3', 'col4', 'col5', 'col6'))
        self.ConsumoComb.heading("#0", text = "Veículo")
        self.ConsumoComb.heading("#1", text = "Data Abastecimento")
        self.ConsumoComb.heading("#2", text = "Motorista")
        self.ConsumoComb.heading("#3", text = "Litros")
        self.ConsumoComb.heading("#4", text = "Km Rodado")
        self.ConsumoComb.heading("#5", text = "Média Km/L")

        self.ConsumoComb.column("#0", width=80)
        self.ConsumoComb.column("#1", width=150)
        #self.ConsumoComb.column("#2", width=70)
        #self.ConsumoComb.column("#3", width=80)
        #self.ConsumoComb.column("#4", width=80)
        #self.ConsumoComb.column("#5", width=80)
        self.ConsumoComb.column("#5", width=90)

        self.ConsumoComb.place(relx=0.00, rely = 0.00, relwidth=1.00, relheight=0.1)

        self.scroolConsumoComb = Scrollbar(self.frameResultado, orient='vertical')
        self.ConsumoComb.configure(yscroll= self.scroolConsumoComb.set)
        self.scroolConsumoComb.place(relx=0.95, rely=0.1, relwidth= 0.04, relheight = 0.85)

Application()

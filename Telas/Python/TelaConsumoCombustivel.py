from tkinter import *
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
        self.TpVeiculo_entry = Entry(self.TelaRelatorio, font=('Segoe UI Semibold', 9), highlightthickness=1, highlightbackground='#BFBFBF')
        self.TpVeiculo_entry.place(relx=0.57, rely=0.23 ,relwidth=0.15, relheight=0.05)


        # Veículo
        self.lb_IdVeiculo= Label(self.TelaRelatorio, text='Id Veículo', font=('Segoe UI Semibold', 10), bg ='#D6FADC', fg='black')
        self.lb_IdVeiculo.place(relx=0.73, rely=0.20, relwidth=0.15, relheight=0.03)
        self.IdVeiculo_entry = Entry(self.TelaRelatorio, font=('Segoe UI Semibold', 9), highlightthickness=1, highlightbackground='#BFBFBF')
        self.IdVeiculo_entry.place(relx=0.73, rely=0.23 ,relwidth=0.15, relheight=0.05)





Application()

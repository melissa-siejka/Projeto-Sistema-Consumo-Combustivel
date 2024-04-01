from sqlalchemy.orm import mapped_column, Mapped, DeclarativeBase, Session
from sqlalchemy import INTEGER, VARCHAR, CHAR, Date, NUMERIC, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.schema import Sequence
from datetime import datetime, date
from tkinter import *
from tkinter import messagebox
import sqlite3

#Realizando o mapeamento da classe CadastroAbastecimento
class CadastroAbastecimento(Base):
    
    __tablename__ = 'abastecimento'
    NReqAbastecimento:Mapped[int]=mapped_column(INTEGER,nullable=False, primary_key=True)
    IdVeiculo:Mapped[int]=mapped_column(INTEGER, ForeignKey(Veiculo.id_veiculo),nullable=False )
    DataAbastecimento:Mapped[datetime]=mapped_column(Date, nullable=False)
    CDMotorista:Mapped [float]=mapped_column(NUMERIC(6),ForeignKey(Motorista.nr_matricula), nullable=False)
    CDTipoCombustivel:Mapped[float]=mapped_column(NUMERIC(3),ForeignKey(TipoCombustivel.cd_tipocombustivel),nullable=False)
    CDPosto:Mapped[float]=mapped_column(NUMERIC(6),ForeignKey(PostoConvenido.CDPosto), nullable=False)
    NRodometro:Mapped[float]=mapped_column(NUMERIC(7),nullable=False) 
    QTLitros:Mapped[float]=mapped_column(NUMERIC(5,2), nullable=False)
    VLCombustivel:Mapped[float]=mapped_column(NUMERIC(5,2), nullable=False)

#Criando Função que vai fazer um novo abastecimento 
    def cadastrarAbastecimento(self, IdVeiculo, CDMotorista, CDPosto,
                               CDTipoCombustivel, NReqAbastecimento, NRodometro, DataAbastecimento, QTLitros, VLCombustivel):
        NovoAbastecimento = CadastroAbastecimento(
                                            IdVeiculo = IdVeiculo,
                                            CDMotorista = CDMotorista,
                                            CDPosto = CDPosto,
                                            CDTipoCombustivel = CDTipoCombustivel,
                                            NReqAbastecimento = NReqAbastecimento, 
                                            NRodometro = NRodometro,
                                            DataAbastecimento = DataAbastecimento,
                                            QTLitros = QTLitros,
                                            VLCombustivel = VLCombustivel)
        Session.add(NovoAbastecimento)
        Session.commit()

# Criando função que vai receber os dados digitados pelo usuario e salvando no banco de dados
        
def Abastecimento():
    IdVeiculo = EntryIdVeiculo.get()
    CDMotorista = EntryCDMotorista.get()
    CDPosto = EntryCDPosto.get()
    CDTipoCombustivel = EntryCDTipoCombustivel.get()
    NReqAbastecimento = EntryNReqAbastecimento.get()
    NRodometro = EntryNRodometro.get()
    DataAbastecimento = EntryDataAbastecimento.get()
    QTLitros = EntryQTLitros.get()
    VLCombustivel = EntryVLCombustivel.get()

# Criando um Novo Abastecimento
    try:
        NovoAbastecimento = CadastroAbastecimento()
        NovoAbastecimento.cadastrarAbastecimento(IdVeiculo = IdVeiculo,
                                            CDMotorista = CDMotorista,
                                            CDPosto = CDPosto,
                                            CDTipoCombustivel = CDTipoCombustivel,
                                            NReqAbastecimento = NReqAbastecimento,
                                            NRodometro = NRodometro,
                                            DataAbastecimento = DataAbastecimento,
                                            QTLitros = QTLitros,
                                            VLCombustivel = VLCombustivel)
# Realizando as verificação, Falta Fazer a culsulta dos resutados armazenados no banco.
        if NRodometro < HodometroAnterior:
            messagebox.showerror("Erro", "Valor de Hodometro Invalido")
        elif QTLitros < QTLitrosAnterior:
            messagebox.showerror("Erro", "Quantidade de litros Invalido")
        else:
            messagebox.showinfo("Cadastro", "Pessoa cadastrada com sucesso!")
    except Exception as e :
        messagebox.showerror("Erro", f"Erro ao cadastrar pessoa: {str(e)}")



janela = Tk()
janela.geometry("800x900")
janela.title("Cadastro de veiculos")
janela.configure(bg="#c5E0B4")
janela.iconbitmap("Imagens\icone_coamo.ico")
#    img = PhotoImage(file="imagens\imagemcoamo.png")
#    Label(janela, image=img).pack()


TituloTela = Label(janela, text="Cadastro De Abastecimento", bg="#c5E0B4", font=("Arial", 20), fg="black")
TituloTela.place(x=100,y=50)

TituloTela = Label(janela, text="Coamo", bg="#c5E0B4", font=("Arial", 120), fg="#1B492B")
TituloTela.place(x=250,y=200)  

LabelRequisicao = Label(janela, text="Número da Requisição", bg="#c5E0B4", font=("Arial", 14), fg="black")
LabelRequisicao.place(x=15,y=100) 
EntryNReqAbastecimento = Entry(janela)
EntryNReqAbastecimento.place(x=15, y=130)

LabelFrota = Label(janela, text="Frota Do Veiculo", bg="#c5E0B4", font=("Arial", 14), fg="black")
LabelFrota.place(x=15,y=150) 
EntryIdVeiculo = Entry(janela)
EntryIdVeiculo.place(x=15, y=180, width=200, height=20)

LabelMatricula = Label(janela, text="Matricula do Motorista", bg="#c5E0B4", font=("Arial", 14), fg="black")
LabelMatricula.place(x=15,y=200 ) 
EntryCDMotorista= Entry(janela)
EntryCDMotorista.place(x=15, y=230)

LabelCodPosto = Label(janela, text="Codigo Do Posto", bg="#c5E0B4", font=("Arial", 14), fg="black")
LabelCodPosto.place(x=15,y=250) 
EntryCDPosto = Entry(janela)
EntryCDPosto.place(x=15, y=280)

LabelHodometro = Label(janela, text="Hodomettro Do Veículo", bg="#c5E0B4", font=("Arial", 14), fg="black")
LabelHodometro.place(x=15,y=300) 
EntryNRodometro = Entry(janela)
EntryNRodometro.place(x=15, y=330)

LabelCodConbustivel = Label(janela, text="Codigo  Do Cobustivel", bg="#c5E0B4", font=("Arial", 14), fg="black")
LabelCodConbustivel.place(x=15,y=350) 
EntryCDTipoCombustivel = Entry(janela)
EntryCDTipoCombustivel.place(x=15, y=380)

LabelValor = Label(janela, text="Valor", bg="#c5E0B4", font=("Arial", 14), fg="black")
LabelValor.place(x=15,y=400) 
EntryVLCombustivel = Entry(janela)
EntryVLCombustivel.place(x=15, y=430)

LabelQantLitro = Label(janela, text="Quantidade de Litros ", bg="#c5E0B4", font=("Arial", 14), fg="black")
LabelQantLitro.place(x=15,y=450) 
EntryQTLitros = Entry(janela)
EntryQTLitros.place(x=15, y=480)

LabelData = Label(janela, text="Data ", bg="#c5E0B4", font=("Arial", 14), fg="black")
LabelData.place(x=15,y=500) 
EntryDataAbastecimento = Entry(janela)
EntryDataAbastecimento.place(x=15, y=530)

BotaoSalvar = Button(janela, text="Salvar", padx=50, pady=10, bd=5, font=("Arial", 12), bg="#1B492B")
BotaoSalvar.place(x=15, y=580)

BotaoSair = Button(janela, text="Sair", padx=50, pady=10, bd=5, font=("Arial", 12), bg="#1B492B")
BotaoSair.place(x=450, y=580)

janela.mainloop()


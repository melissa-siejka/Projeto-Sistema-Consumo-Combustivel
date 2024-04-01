from sqlalchemy.orm import mapped_column, Mapped, DeclarativeBase, Session
from sqlalchemy import INTEGER, VARCHAR, CHAR, Date, NUMERIC, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.schema import Sequence
from datetime import datetime, date
from tkinter import *
from tkinter import messagebox
import sqlite3

# Mapeamento da classe Motorista
class Motorista(Base):
    __tablename__ = 'motorista'
    NRMatricula:Mapped[float]=mapped_column(NUMERIC(6),Sequence('TIPO_COMBUSTIVEL_SEQ'),nullable=False,primary_key=True)
    NRCnh:Mapped[float]=mapped_column(NUMERIC(9),nullable=False, unique=True)
    TPCategoria:Mapped[str]=mapped_column(VARCHAR(2),nullable=False)
    CDCargo:Mapped[float]=mapped_column(NUMERIC(3), ForeignKey(CargoMotorista.cd_cargo), nullable=False)
    DTAdmissao:Mapped[date]=mapped_column(Date, nullable=False)
    DTDesligamento:Mapped[date]=mapped_column(Date)
    INAtivo:Mapped[str]=mapped_column(CHAR(1),nullable=False)
    IDPessoa:Mapped[float]=mapped_column(NUMERIC(7,2), ForeignKey(Pessoa.id_pessoa), nullable=False)

    def CadastroMotorista(self, NRCnh, TPCategoria, CDCargo, DTAdmissao, DTDesligamento,  INAtivo, IDPessoa ):
        NovoMotorista = Motorista(NRCnh = NRCnh,
                                TPCategoria = TPCategoria,
                                CDCargo = CDCargo,
                                DTAdmissao = DTAdmissao,
                                DTDesligamento = DTDesligamento, 
                                INAtivo = INAtivo,
                                IDPessoa = IDPessoa)
        Session.add(NovoMotorista)
        Session.commit()

def CadMotorista():
    NRCnh = EntryNRCnh.get()
    TPCategoria = EntryTPCategoria.get()
    CDCargo = EntryCDCargo.get()
    DTAdmissao = EntryDTAdmissao.get()
    DTDesligamento = EntryDTDesligamento.get()
    INAtivo = EntryINAtivo.get()
    IDPessoa = EntryIDPessoa.get()

# Criando um Novo Motorista
    try:
        NovoMotorista = Motorista()
        NovoMotorista.CadastroMotorista(NRCnh= NRCnh,
                                            TPCategoria = TPCategoria,
                                            CDCargo = CDCargo,
                                            DTAdmissao  = DTAdmissao,
                                            DTDesligamento = DTDesligamento,
                                            INAtivo = INAtivo,
                                            IDPessoa = IDPessoa)
        messagebox.showinfo("Cadastro", "Pessoa cadastrada com sucesso!")
    except Exception as e :
        messagebox.showerror("Erro", f"Erro ao cadastrar pessoa: {str(e)}")
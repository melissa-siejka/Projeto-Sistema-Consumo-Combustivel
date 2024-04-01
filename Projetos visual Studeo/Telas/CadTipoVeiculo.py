from sqlalchemy.orm import mapped_column, Mapped, DeclarativeBase, Session
from sqlalchemy import INTEGER, VARCHAR, CHAR, Date, NUMERIC, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.schema import Sequence
from datetime import datetime, date
from tkinter import *
from tkinter import messagebox
import sqlite3


class TipoVeiculo(Base):
    __tablename__ = 'tipo_veiculo'
    CDTipoVeiculo:Mapped[float]=mapped_column(NUMERIC(3),Sequence('TIPO_VEICULO_SEQ'),primary_key=True ,nullable=False)
    DSTipoVeiculo:Mapped[str]=mapped_column(VARCHAR(50))
    

    def CadTipoVeiculo(self, DSTipoVeiculo):
        cadastrar = TipoVeiculo(DSTipoVeiculo = DSTipoVeiculo)
        Session.add(cadastrar)
        Session.commit()
        return cadastrar

def CadastrarTipoVeiculo():
    NovoTipo = EntryTipoVeiculo.get()


    try:
        NovoTipoVeiculo = TipoVeiculo()
        NovoTipoVeiculo.CadTipoVeiculo(DSTipoVeiculo = NovoTipo)
        messagebox.showinfo("Cadastro", "Novo Tipo cadastrado com sucesso!")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao cadastrar novo Tipo de veiculo!: {str(e)}")
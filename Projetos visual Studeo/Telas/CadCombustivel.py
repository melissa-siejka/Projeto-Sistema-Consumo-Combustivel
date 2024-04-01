from sqlalchemy.orm import mapped_column, Mapped, DeclarativeBase, Session
from sqlalchemy import INTEGER, VARCHAR, CHAR, Date, NUMERIC, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.schema import Sequence
from datetime import datetime, date
from tkinter import *
from tkinter import messagebox
import sqlite3


class TipoCombustivel(Base):
    __tablename__ = 'tipo_combustivel'
    CDTipoCombustivel:Mapped[float]=mapped_column(NUMERIC(3),Sequence('TIPO_COMBUSTIVEL_SEQ'),primary_key=True, nullable=False)
    DSTipoCombustivel:Mapped[str]=mapped_column(VARCHAR(50), nullable=False)


    

    def CadastrarCombustivel(self, DSTipoCombustivel):
        cadastrar = TipoCombustivel(DSTipoCombustivel = DSTipoCombustivel)
        Session.add(cadastrar)
        Session.commit()
        return cadastrar

def cadastrar_combustivel():
    NomeCombustivel = EntryEombustivel.get()


    try:
        NovoCombustivel = TipoCombustivel()
        NovoCombustivel.CadastrarCombustivel(DSTipoCombustivel = NomeCombustivel)
        messagebox.showinfo("Cadastro", "Combustivel cadastrado com sucesso!")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao cadastrar Combustivel : {str(e)}")

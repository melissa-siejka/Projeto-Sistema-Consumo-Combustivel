from sqlalchemy.orm import mapped_column, Mapped, DeclarativeBase, Session
from sqlalchemy import INTEGER, VARCHAR, CHAR, Date, NUMERIC, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.schema import Sequence
from datetime import datetime, date
from tkinter import *
from tkinter import messagebox
import sqlite3


class CargoMotorista(Base):
    __tablename__ = "CargoMotorista"
    CDCargo:Mapped[float]=mapped_column(NUMERIC(3),Sequence('CARGO_MOTORISTA_SEQ'),nullable=False, primary_key=True)
    DSCargo:Mapped[str]=mapped_column(VARCHAR(50))

    def CadastrarCargo(self, DSCargo):
        NovoCargo = CargoMotorista(DSCargo = DSCargo)
        Session.add(NovoCargo)
        Session.commit()
        return NovoCargo

def CadastrarCargo():
    Cargo = EntryCargo.get()


    try:
        NovoCargo = CargoMotorista()
        NovoCargo.CadastrarCargo(DSCargo = Cargo)
        messagebox.showinfo("Cadastro", "Novo cargo cadastrado com sucesso!")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao cadastrar cargo : {str(e)}")

Janela = Tk()
Janela.geometry("800x900")
Janela.title("Cadastro de Pessoas")
Janela.configure(bg="#c5E0B4")
Janela.iconbitmap("Imagens\\icone_coamo.ico")


            
LabelCargo= Label(Janela, text="Novo Cargo:")
LabelCargo.grid(row=0, column=0)
EntryCargo= Entry(Janela)
EntryCargo.grid(row=0, column=1)


ButtonCadastrar = Button(Janela, text="Cadastrar", command=CadastrarCargo)
ButtonCadastrar.grid(row=4, columnspan=2)

Janela.mainloop()


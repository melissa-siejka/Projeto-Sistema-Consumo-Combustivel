from sqlalchemy.orm import mapped_column, Mapped, DeclarativeBase, Session
from sqlalchemy import INTEGER, VARCHAR, CHAR, Date, NUMERIC, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.schema import Sequence
from datetime import datetime, date
from tkinter import *
from tkinter import messagebox
import sqlite3


class Unidade(Base):
    __tablename__ = 'unidade'
    CDUnidade:Mapped[float]=mapped_column(NUMERIC(6),Sequence('UNIDADE_SEQ'),nullable=False, primary_key=True, unique=True)
    INAtivo:Mapped[str]=mapped_column(CHAR(1), nullable=False)
    NMMunicipio:Mapped[str]=mapped_column(VARCHAR(50), nullable=False)
    IDPessoa:Mapped[float]=mapped_column(NUMERIC(7,2), ForeignKey(Pessoa.id_pessoa), nullable=False)

    def CadastroUnidade(self, INAtivo, NMMunicipio, IDPessoa):
        NovaUnidade = Unidade(  INAtivo = INAtivo,
                                NMMunicipio = NMMunicipio,
                                IDPessoa = IDPessoa,
                                )
        Session.add(NovaUnidade)
        Session.commit()

def CadUnidade():
    INAtivo= EntryINAtivo.get()
    NMMunicipio = EntryNMMunicipio.get()
    IDPessoa = EntryIDPessoa.get()

# Criando um Novo Motorista
    try:
        NovaUnidade = Unidade()
        NovaUnidade.CadastroUnidade(INAtivo = INAtivo,
                                    NMMunicipio = NMMunicipio,
                                    IDPessoa = IDPessoa)
        
        messagebox.showinfo("Cadastro", "Unidade cadastrada com sucesso!")
    except Exception as e :
        messagebox.showerror("Erro", f"Erro ao cadastrar unidade: {str(e)}")

janela = Tk()
janela.geometry("800x900")
janela.title("Cadastro de veiculos")
janela.configure(bg="#c5E0B4")
janela.iconbitmap("Imagens\icone_coamo.ico")
#img = PhotoImage(file="imagens\imagemcoamo.png")
#Label(janela, image=img).pack()


titulo_tela = Label(janela, text="Cadastro De Unidade", bg="#c5E0B4", font=("Arial", 20), fg="black")
titulo_tela.place(x=100,y=50)

TituloTela = Label(janela, text="Coamo", bg="#c5E0B4", font=("Arial", 120), fg="#1B492B")
TituloTela.place(x=250,y=200)  


LabelINAtivo = Label(janela, text="Status:", bg="#c5E0B4", font=("Arial", 14), fg="black")
LabelINAtivo.place(x=15,y=100) 
EntryINAtivo = Entry(janela)
EntryINAtivo.place(x=15, y=130)

LabelNMMunicipio = Label(janela, text="Nome do Municipio", bg="#c5E0B4", font=("Arial", 14), fg="black")
LabelNMMunicipio.place(x=15,y=150) 
EntryNMMunicipio = Entry(janela)
EntryNMMunicipio .place(x=15, y=180)

LabaelIDPessoa = Label(janela, text="Nome", bg="#c5E0B4", font=("Arial", 14), fg="black")
LabaelIDPessoa.place(x=15,y=200 ) 
EntryIDPessoa = Entry(janela)
EntryIDPessoa.place(x=15, y=230)

BotaoSalvar = Button(janela, text="Salvar", padx=50, pady=10, bd=5, font=("Arial", 12), bg="#1B492B")
BotaoSalvar.place(x=15, y=580)

BotaoSair = Button(janela, text="Sair", padx=50, pady=10, bd=5, font=("Arial", 12), bg="#1B492B")
BotaoSair.place(x=450, y=580)



janela.mainloop()


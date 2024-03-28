from datetime import *
from urllib.parse import quote
from sqlalchemy import create_engine, text
from sqlalchemy.orm import scoped_session, sessionmaker, declarative_base, Session, mapped_column, Mapped
from sqlalchemy import INTEGER, VARCHAR, CHAR, Date, NUMERIC, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.schema import Sequence
from Pessoa import Pessoa
from ConectBD.ConexaoBancoDeDados import Base


class PostoConvenido(Base):
    __tablename__ = 'posto_conveniado'
    cd_posto:Mapped[float]=mapped_column(NUMERIC(6),Sequence('POSTO_CONVENIADO_SEQ'),nullable=False, primary_key=True, unique=True)
    id_pessoa:Mapped[float]=mapped_column(NUMERIC(7,2), ForeignKey(Pessoa.id_pessoa), nullable=False)
    nm_posto:Mapped[str]=mapped_column(VARCHAR(50),nullable=False)
    cnpj:Mapped[str]=mapped_column(VARCHAR(14),nullable=False, unique=True)
    dt_convenio:Mapped[date]=mapped_column(Date,nullable=False)


from tkinter import *
import sqlite3



def Cadastrar(nome, cnpj, codigo, data, status):
    nome  = nome.get()
    cnpj = cnpj.get()
    codigo = codigo.get()
    data= data.get()
    status = status.get()


    cadastro = session.execute("INSERT INTO ABASTECIMENTO (cd_posto, nm_posto,  cnpj, dt_convenio, in_ativo) VALUES(?, ?, ?, ?, ?)"(codigo, nome, cnpj, data, status))

    session.add(cadastro)


def TelaCadastroPosto():
    janela = Tk()
    janela.geometry("800x900")
    janela.title("Cadastro de veiculos")
    janela.configure(bg="#c5E0B4")
    janela.iconbitmap("Imagens\icone_coamo.ico")
#    img = PhotoImage(file="imagens\imagemcoamo.png")
#    Label(janela, image=img).pack()


    titulo_tela = Label(janela, text="Cadastro De Posto", bg="#c5E0B4", font=("Arial", 20), fg="black")
    titulo_tela.place(x=100,y=50)

    titulo_tela = Label(janela, text="Coamo", bg="#c5E0B4", font=("Arial", 120), fg="#1B492B")
    titulo_tela.place(x=600,y=200)  


    LabelNomeP = Label(janela, text="Nome Do Posto", bg="#c5E0B4", font=("Arial", 14), fg="black")
    LabelNomeP.place(x=15,y=100) 
    InputiNomeP = Entry(janela)
    InputiNomeP.place(x=15, y=130)

    labelCNPJ= Label(janela, text="CNPJ", bg="#c5E0B4", font=("Arial", 14), fg="black")
    labelCNPJ.place(x=15,y=150) 
    inputCNPJ = Entry(janela)
    inputCNPJ.place(x=15, y=180)

    labelCodigoP = Label(janela, text="Codigo", bg="#c5E0B4", font=("Arial", 14), fg="black")
    labelCodigoP.place(x=15,y=200 ) 
    inputCodigoP = Entry(janela)
    inputCodigoP.place(x=15, y=230)

    labelData= Label(janela, text="Data", bg="#c5E0B4", font=("Arial", 14), fg="black")
    labelData.place(x=15,y=250) 
    inputData = Entry(janela)
    inputData.place(x=15, y=280)

    labelSatus = Label(janela, text="Status", bg="#c5E0B4", font=("Arial", 14), fg="black")
    labelSatus.place(x=15,y=300) 
    inputStatus = Entry(janela)
    inputStatus.place(x=15, y=330)

    botao_sair = Button(janela, text="Sair", padx=50, pady=10, bd=5, font=("Arial", 12), bg="#1B492B")
    botao_sair.place(x=350, y=500)

    botao_cadastrar = Button(janela, text="Salvar", padx=50, pady=10, bd=5, font=("Arial", 12), bg="#1B492B", command=Cadastrar(nome=LabelNomeP, cnpj=labelCNPJ,codigo=inputCodigoP, data=inputData, status=inputStatus ))
    botao_cadastrar.place(x=15, y=500)


    janela.mainloop()

TelaCadastroPosto()

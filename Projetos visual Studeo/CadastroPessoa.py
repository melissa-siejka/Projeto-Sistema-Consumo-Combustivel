import cx_Oracle
from sqlalchemy.ext.declarative import declarative_base
from urllib.parse import quote
from sqlalchemy import create_engine, text
from sqlalchemy.orm import scoped_session, sessionmaker, DeclarativeBase, Session
from tkinter import *
from tkinter import messagebox

lib_dir = r"C:\Users\mayqu\APP Oracle\instantclient_21_13"
cx_Oracle.init_oracle_client(lib_dir=lib_dir)

USER = 'CADPESSOA'
PASSWD = quote('admin')
HOST = 'localhost'
PORT = 1521
SID = "xe"
sid = cx_Oracle.makedsn(HOST, PORT, sid=SID)
instance = f"oracle+cx_oracle://{USER}:{PASSWD}@{sid}"
engine = create_engine(url=instance, echo=True, max_identifier_length=30)
session = scoped_session(sessionmaker(bind=engine, autoflush=True, autocommit=False))



from sqlalchemy.orm import mapped_column, Mapped, DeclarativeBase
from sqlalchemy import INTEGER, VARCHAR, CHAR, Date, NUMERIC, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.schema import Sequence
from datetime import datetime, date

class Base(DeclarativeBase):
    pass



class Pessoa(Base):
    __tablename__ = 'PESSOA'
    ID:Mapped[float] = mapped_column(NUMERIC(6), primary_key=True, nullable=False)
    NOME:Mapped[str] = mapped_column(VARCHAR(50), nullable=False)
    CPF:Mapped[str] = mapped_column(VARCHAR(11), nullable=False)
    ENDERECO:Mapped[str] = mapped_column(VARCHAR(100), nullable=False)
    TELEFONE:Mapped[str] = mapped_column(VARCHAR(11), nullable=False)

    def CadastrarPessoa(self, ID, NOME, CPF, ENDERECO, TELEFONE):
        cadastrar = Pessoa(ID = ID,
                           NOME = NOME,
                           CPF = CPF,
                           ENDERECO = ENDERECO,
                           TELEFONE = TELEFONE
                           )
        session.add(cadastrar)
        session.commit()
        return cadastrar

def cadastrar_pessoa():
    nome = entry_nome.get()
    cpf = entry_cpf.get()
    endereco = entry_endereco.get()
    telefone = entry_telefone.get()

    try:
        # Supondo que você tenha a instância da classe Pessoa já criada
        pessoa = Pessoa()   
        pessoa.CadastrarPessoa(ID=None, NOME=nome, CPF=cpf, ENDERECO=endereco, TELEFONE=telefone)
        messagebox.showinfo("Cadastro", "Pessoa cadastrada com sucesso!")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao cadastrar pessoa: {str(e)}")


tela = Tk()
tela.geometry("400x200")
tela.title("Cadastro de Pessoa")
tela.configure(bg="#8ab54e")

label_nome = Label(tela, text="Nome:")
label_nome.grid(row=0, column=0)
entry_nome = Entry(tela)
entry_nome.grid(row=0, column=1)

label_cpf = Label(tela, text="CPF:")
label_cpf.grid(row=1, column=0)
entry_cpf = Entry(tela)
entry_cpf.grid(row=1, column=1)

label_endereco = Label(tela, text="Endereço:")
label_endereco.grid(row=2, column=0)
entry_endereco = Entry(tela)
entry_endereco.grid(row=2, column=1)

label_telefone = Label(tela, text="Telefone:")
label_telefone.grid(row=3, column=0)
entry_telefone = Entry(tela)
entry_telefone.grid(row=3, column=1)

button_cadastrar = Button(tela, text="Cadastrar", command=cadastrar_pessoa)
button_cadastrar.grid(row=4, columnspan=2)

tela.mainloop()
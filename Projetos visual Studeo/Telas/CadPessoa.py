from sqlalchemy.orm import mapped_column, Mapped, DeclarativeBase, Session
from sqlalchemy import Column, VARCHAR, CHAR, Date, NUMERIC, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.schema import Sequence
from datetime import datetime, date
from tkinter import *
from tkinter import messagebox

from sqlalchemy import Column, VARCHAR, CHAR, Date, NUMERIC, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session

Base = declarative_base()

class Pessoa(Base):
    __tablename__ = "pessoa"
    IDPessoa:Mapped[float] = mapped_column(NUMERIC(7), Sequence('PESSOA_SEQ'), nullable=False, primary_key = True, unique=True)
    NMPessoa:Mapped[str] = mapped_column(VARCHAR(100), nullable=False)
    NRCpfCnpj:Mapped[str] = mapped_column(CHAR(14), nullable=False, unique=True)
    NRCep:Mapped[str] = mapped_column(CHAR(8), nullable=False)
    DSEndereco:Mapped[str] = mapped_column(VARCHAR(200), nullable=False)

  
    def CadastrarPessoa(self, NMPessoa, NRCpfCnpj,  NRCep, DSEndereco):
        cadastrar = Pessoa(NMPessoa = NMPessoa, 
                           NRCpfCnpj = NRCpfCnpj, 
                           NRCep = NRCep, 
                           DSEndereco = DSEndereco)
       
        Session.add(cadastrar)
        Session.commit()
        return cadastrar


def cadastrar_pessoa():
    nome = entry_nome.get()
    cpfCnpj = entry_cpfCnpj.get()
    cep = entry_cep.get()
    endereco = entry_endereco.get()
    try:
        pessoa = Pessoa()
        pessoa.CadastrarPessoa(NMPessoa = nome, 
                               NRCpfCnpj = cpfCnpj, 
                               NRCep  = cep, 
                               DSEndereco = endereco)
        
        messagebox.showinfo("Cadastro", "Pessoa cadastrada com sucesso!")
        
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao cadastrar pessoa: {str(e)}")

janela = Tk()
janela.geometry("800x900")
janela.title("Cadastro de Pessoas")
janela.configure(bg="#c5E0B4")
janela.iconbitmap("Imagens\icone_coamo.ico")


            
label_nome = Label(janela, text="Nome:")
label_nome.grid(row=0, column=0)
entry_nome = Entry(janela)
entry_nome.grid(row=0, column=1)

label_cpfCnpj = Label(janela, text="CPF:")
label_cpfCnpj.grid(row=1, column=0)
entry_cpfCnpj= Entry(janela)
entry_cpfCnpj.grid(row=1, column=1)

label_endereco = Label(janela, text="Endereço:")
label_endereco.grid(row=2, column=0)
entry_endereco = Entry(janela)
entry_endereco.grid(row=2, column=1)

label_cep = Label(janela, text="CEP:")
label_cep.grid(row=3, column=0)
entry_cep = Entry(janela)
entry_cep.grid(row=3, column=1)

button_cadastrar = Button(janela, text="Cadastrar", command=cadastrar_pessoa)
button_cadastrar.grid(row=4, columnspan=2)

janela.mainloop()

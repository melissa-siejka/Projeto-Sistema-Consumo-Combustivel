
#class CDBanco():
import cx_Oracle
from sqlalchemy.ext.declarative import declarative_base
from urllib.parse import quote
from sqlalchemy import create_engine, text
from sqlalchemy.orm import scoped_session, sessionmaker, DeclarativeBase, Session

lib_dir = r"C:\Users\mayqu\APP Oracle\instantclient_21_13"
cx_Oracle.init_oracle_client(lib_dir=lib_dir)

USER = 'PROJETO_ABASTECIMENTO'
PASSWD = quote('admin')
HOST = 'localhost'
PORT = 1521
SID = "xe"
sid = cx_Oracle.makedsn(HOST, PORT, sid=SID)
instance = f"oracle+cx_oracle://{USER}:{PASSWD}@{sid}"
engine = create_engine(url=instance, echo=True, max_identifier_length=30)
session = scoped_session(sessionmaker(bind=engine, autoflush=True, autocommit=False))

#cad = Session.execute(text("INSERT INTO POSTO_CONVENIADO (cd_posto, nm_posto, cnpj, dt_convenio, in_ativo) VALUES( 'Andrade', '12365498712545', '22/03/2023', 't') );"))
        

#teste = session.execute(text('SELECT * FROM pessoa'))

#for i in teste:
#    print(i)

from sqlalchemy.orm import mapped_column, DeclarativeBase
from sqlalchemy import INTEGER, VARCHAR, CHAR, Date, NUMERIC, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.schema import Sequence
from datetime import datetime, date
from tkinter import *
from tkinter import messagebox


class Base(DeclarativeBase):
    pass
from sqlalchemy import Column, Integer, String, Numeric, Sequence, CHAR, Date
from sqlalchemy.orm import relationship

class Pessoa(Base):
    __tablename__ = "pessoa"
    id_pessoa = Column(Numeric(7), Sequence('PESSOA_SEQ'), nullable=False, primary_key=True)
    nm_pessoa = Column(String(100), nullable=False)
    nr_cpfcnpj = Column(CHAR(14), nullable=False)
    nr_cep = Column(CHAR(8), nullable=False)
    ds_endereco = Column(String(200), nullable=False)

#     def CadastrarPessoa(self, nm_pessoa, nr_cpfcnpj,  nr_cep, ds_endereco):
#         cadastrar = Pessoa(nm_pessoa = nm_pessoa,
#                            nr_cpfcnpj = nr_cpfcnpj,
#                            ds_endereco = ds_endereco,
#                            nr_cep = nr_cep
                           
#                            )
#         session.add(cadastrar)
#         session.commit()
#         return cadastrar

# def cadastrar_pessoa():
#     nome = entry_nome.get()
#     cpfCnpj = entry_cpfCnpj.get()
#     endereco = entry_endereco.get()
#     cep = entry_cep.get()

#     try:
#         pessoa = Pessoa()
#         pessoa.CadastrarPessoa(nm_pessoa= nome, nr_cpfcnpj= cpfCnpj, ds_endereco= endereco, nr_cep= cep)
#         messagebox.showinfo("Cadastro", "Pessoa cadastrada com sucesso!")
#     except Exception as e:
#         messagebox.showerror("Erro", f"Erro ao cadastrar pessoa: {str(e)}")

# janela = Tk()
# janela.geometry("800x900")
# janela.title("Cadastro de Pessoas")
# janela.configure(bg="#c5E0B4")
# janela.iconbitmap("Imagens\\icone_coamo.ico")


            
# label_nome = Label(janela, text="Nome:")
# label_nome.grid(row=0, column=0)
# entry_nome = Entry(janela)
# entry_nome.grid(row=0, column=1)

# label_cpfCnpj = Label(janela, text="CPF:")
# label_cpfCnpj.grid(row=1, column=0)
# entry_cpfCnpj= Entry(janela)
# entry_cpfCnpj.grid(row=1, column=1)

# label_endereco = Label(janela, text="Endereço:")
# label_endereco.grid(row=2, column=0)
# entry_endereco = Entry(janela)
# entry_endereco.grid(row=2, column=1)

# label_cep = Label(janela, text="CEP:")
# label_cep.grid(row=3, column=0)
# entry_cep = Entry(janela)
# entry_cep.grid(row=3, column=1)

# button_cadastrar = Button(janela, text="Cadastrar", command=cadastrar_pessoa)
# button_cadastrar.grid(row=4, columnspan=2)

# janela.mainloop()




# class TipoCombustivel(Base):
#     __tablename__ = "tipo_combustivel"
#     cd_tipocombustivel = Column(Numeric(3),Sequence('TIPO_COMBUSTIVEL_SEQ'),primary_key=True, nullable=False)
#     ds_tipocombustivel = Column(String(50), nullable=False)


#     def CadastrarCombustivel(self, ds_tipocombustivel):
#         cadastrar = TipoCombustivel(ds_tipocombustivel = ds_tipocombustivel)
#         session.add(cadastrar)
#         session.commit()
#         return cadastrar

# def cadastrar_combustivel():
#     tipo_combustivel = entry_combustivel.get()


#     try:
#         combustivel = TipoCombustivel()
#         combustivel.CadastrarCombustivel(ds_tipocombustivel= tipo_combustivel)
#         messagebox.showinfo("Cadastro", "Combustivel cadastrado com sucesso!")
#     except Exception as e:
#         messagebox.showerror("Erro", f"Erro ao cadastrar Combustivel : {str(e)}")

# janela = Tk()
# janela.geometry("800x900")
# janela.title("Cadastro de Pessoas")
# janela.configure(bg="#c5E0B4")
# janela.iconbitmap("Imagens\\icone_coamo.ico")


            
# label_combustivel= Label(janela, text="Tipo De Combustivel:")
# label_combustivel.grid(row=0, column=0)
# entry_combustivel= Entry(janela)
# entry_combustivel.grid(row=0, column=1)


# button_cadastrar = Button(janela, text="Cadastrar", command=cadastrar_combustivel)
# button_cadastrar.grid(row=4, columnspan=2)

# janela.mainloop()


class CargoMotorista(Base):
    __tablename__ = "cargo_motorista"
    cd_cargo = Column(Numeric(3),Sequence('CARGO_MOTORISTA_SEQ'),nullable=False, primary_key=True)
    ds_cargo = Column(String(50))

    
#     def CadastrarCargo(self, ds_cargo):
#         novoCargo = CargoMotorista(ds_cargo = ds_cargo)
#         session.add(novoCargo)
#         session.commit()
#         return novoCargo

# def cadastrarCargo():
#     cargo = entry_cargo.get()


#     try:
#         NovoCargo = CargoMotorista()
#         NovoCargo.CadastrarCargo(ds_cargo= cargo)
#         messagebox.showinfo("Cadastro", "Novo cargo cadastrado com sucesso!")
#     except Exception as e:
#         messagebox.showerror("Erro", f"Erro ao cadastrar cargo : {str(e)}")

# janela = Tk()
# janela.geometry("800x900")
# janela.title("Cadastro de Pessoas")
# janela.configure(bg="#c5E0B4")
# janela.iconbitmap("Imagens\\icone_coamo.ico")


            
# label_cargo= Label(janela, text="Novo Cargo:")
# label_cargo.grid(row=0, column=0)
# entry_cargo= Entry(janela)
# entry_cargo.grid(row=0, column=1)


# button_cadastrar = Button(janela, text="Cadastrar", command=cadastrarCargo)
# button_cadastrar.grid(row=4, columnspan=2)

# janela.mainloop()
    

class TipoVeiculo(Base):
    __tablename__ = "tipo_veiculo"
    cd_tipoveiculo = Column(Numeric(3),Sequence('TIPO_VEICULO_SEQ'),primary_key=True ,nullable=False)
    ds_tipoveiculo = Column(String(50))

    def CadastrarTipoVeiculo(self, ds_tipoveiculo):
        novoTipo = TipoVeiculo(ds_tipoveiculo = ds_tipoveiculo)
        session.add(novoTipo)
        session.commit()
        return novoTipo

def cadastrarTipoVeiculo():
    tipoVeiculo = entry_veiculo.get()


    try:
        NovoTipo = TipoVeiculo()
        NovoTipo.CadastrarTipoVeiculo(ds_tipoveiculo = tipoVeiculo)
        messagebox.showinfo("Cadastro", "Novo Tipo de veículo cadastrado com sucesso!")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao cadastrar o tipo do veículo : {str(e)}")

janela = Tk()
janela.geometry("800x900")
janela.title("Cadastro do tipo de veículo")
janela.configure(bg="#c5E0B4")
janela.iconbitmap("Imagens\\icone_coamo.ico")


            
label_tipoVeiculo= Label(janela, text="Novo Tipo:")
label_tipoVeiculo.grid(row=0, column=0)
entry_veiculo= Entry(janela)
entry_veiculo.grid(row=0, column=1)


button_cadastrar = Button(janela, text="Cadastrar", command=cadastrarTipoVeiculo)
button_cadastrar.grid(row=4, columnspan=2)

janela.mainloop()
        

class Unidade(Base):
    __tablename__ = 'unidade'
    cd_unidade = Column(Numeric(6),Sequence('UNIDADE_SEQ'),nullable=False, primary_key=True, unique=True)
    id_pessoa = Column(Numeric(7,2), ForeignKey(Pessoa.id_pessoa), nullable=False)
    nm_unidade = Column(String(50), nullable=False)
    nr_cep = Column(CHAR(7), nullable=False)
    in_ativa = Column(CHAR(1), nullable=False)
    ds_endereco = Column(String(200), nullable=False)
    cnpj = Column(CHAR(14), nullable=False)
    nm_municipio = Column(String(50), nullable=False)
    pessoa = relationship("Pessoa")

class Motorista(Base):
    __tablename__ = 'motorista'
    nr_matricula = Column(Numeric(6),Sequence('TIPO_COMBUSTIVEL_SEQ'),nullable=False,primary_key=True)
    nm_motorista = Column(String(50),nullable=False)
    nr_cpf = Column(String(11),nullable=False, unique=True)
    nr_cnh = Column(Numeric(9),nullable=False, unique=True)
    tp_categoria = Column(String(2),nullable=False)
    cd_cargo = Column(Numeric(3), ForeignKey('cargo_motorista.cd_cargo'), nullable=False)
    id_pessoa = Column(Numeric(7,2), ForeignKey('pessoa.id_pessoa'), nullable=False)
    dt_admissao = Column(Date, nullable=False)
    dt_desligamento = Column(Date)
    in_ativo = Column(CHAR(1),nullable=False)

class PostoConvenido(Base):
    __tablename__ = 'posto_conveniado'
    cd_posto = Column(Numeric(6),Sequence('POSTO_CONVENIADO_SEQ'),nullable=False, primary_key=True, unique=True)
    id_pessoa = Column(Numeric(7,2), ForeignKey('pessoa.id_pessoa'), nullable=False)
    nm_posto = Column(String(50),nullable=False)
    cnpj = Column(String(14),nullable=False, unique=True)
    dt_convenio = Column(Date,nullable=False)

class UnidadeVeiculo(Base):
    __tablename__ = 'unidade_veiculo'
    id_veiculo = Column(Numeric(7),nullable=False,primary_key=True,unique=True)
    cd_unidade = Column(Numeric(6), ForeignKey('unidade.cd_unidade'), nullable=False)
    dt_vinculo = Column(Date, nullable=False)
    dt_desvinculo = Column(Date)

class Veiculo(Base):
    __tablename__ = 'veiculo'
    id_veiculo = Column(Numeric(7), Sequence('VEICULO_SEQ'),nullable=False, primary_key=True,unique=True)
    nr_placa = Column(CHAR(7),nullable=False, unique=True)
    dt_aquisicao = Column(Date, nullable=False)
    dt_baixa = Column(Date)
    qt_capacidadetanque = Column(Integer, nullable=False)
    in_ativo = Column(CHAR(1),nullable=False)
    cd_unidade = Column(Numeric(6), ForeignKey('unidade.cd_unidade'), nullable=False)
    cd_tipoveiculo = Column(Numeric(3), ForeignKey('tipo_veiculo.cd_tipoveiculo'), nullable=False)
    cd_tipocombustivel = Column(Numeric(3), ForeignKey('tipo_combustivel.cd_tipocombustivel'), nullable=False)

class VeiculoMotorista(Base):
    __tablename__ = 'veiculo_motorista'
    id_veiculo = Column(Numeric(7),nullable=False,primary_key=True, unique=True)
    cd_motorista = Column(Numeric(6), ForeignKey('motorista.nr_matricula'), nullable=False)
    dt_vinculo = Column(Date,nullable=False)
    dt_desvinculo = Column(Date)

class Abastecimento(Base):
    __tablename__ = 'abastecimento'
    id_veiculo = Column(Integer, ForeignKey('veiculo.id_veiculo'),nullable=False )
    cd_motorista = Column(Numeric(6),ForeignKey('motorista.nr_matricula'), nullable=False)
    cd_posto = Column(Numeric(6),ForeignKey('posto_conveniado.cd_posto'), nullable=False)
    cd_tipocombustivel = Column(Numeric(3),ForeignKey('tipo_combustivel.cd_tipocombustivel'),nullable=False)
    nr_reqastecimento = Column(Integer,nullable=False, primary_key=True)
    nr_hodometro = Column(Numeric(7),nullable=False)
    dt_abastecimento = Column(Date, nullable=False)  
    qt_litros = Column(Numeric(5,2), nullable=False)
    vl_combustivel = Column(Numeric(5,2), nullable=False)

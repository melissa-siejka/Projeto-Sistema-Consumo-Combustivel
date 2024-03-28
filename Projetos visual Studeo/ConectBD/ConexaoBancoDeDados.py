
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

from sqlalchemy.orm import mapped_column, Mapped, DeclarativeBase
from sqlalchemy import INTEGER, VARCHAR, CHAR, Date, NUMERIC, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.schema import Sequence
from datetime import datetime, date

class Base(DeclarativeBase):
    pass

class Pessoa(Base):
    __tablename__ = 'pessoa'
    id_pessoa:Mapped[float]=mapped_column(NUMERIC(7,2),Sequence('PESSOA_SEQ'), nullable=False, primary_key=True, unique=True)
    nm_pessoa:Mapped[str]=mapped_column(VARCHAR(100), nullable=False)
    nr_cpfcnpj:Mapped[str]=mapped_column(CHAR(14), nullable=False,unique=True)
    nr_cep:Mapped[str]=mapped_column(CHAR(8), nullable=False)
    ds_endereco:Mapped[str]=mapped_column(VARCHAR(200), nullable=False)

class TipoCombustivel(Base):
    __tablename__ = 'tipo_combustivel'
    cd_tipocombustivel:Mapped[float]=mapped_column(NUMERIC(3),Sequence('TIPO_COMBUSTIVEL_SEQ'),primary_key=True, nullable=False)
    ds_tipocombustivel:Mapped[str]=mapped_column(VARCHAR(50), nullable=False)

class CargoMotorista(Base):
    __tablename__ = "cargo_motorista"
    cd_cargo:Mapped[float]=mapped_column(NUMERIC(3),Sequence('CARGO_MOTORISTA_SEQ'),nullable=False, primary_key=True)
    ds_cargo:Mapped[str]=mapped_column(VARCHAR(50))


class TipoVeiculo(Base):
    __tablename__ = 'tipo_veiculo'
    cd_tipoveiculo:Mapped[float]=mapped_column(NUMERIC(3),Sequence('TIPO_VEICULO_SEQ'),primary_key=True ,nullable=False)
    ds_tipoveiculo:Mapped[str]=mapped_column(VARCHAR(50))


class Unidade(Base):
    __tablename__ = 'unidade'
    cd_unidade:Mapped[float]=mapped_column(NUMERIC(6),Sequence('UNIDADE_SEQ'),nullable=False, primary_key=True, unique=True)
    id_pessoa:Mapped[float]=mapped_column(NUMERIC(7,2), ForeignKey(Pessoa.id_pessoa), nullable=False)
    nm_unidade:Mapped[str]=mapped_column(VARCHAR(50), nullable=False)
    nr_cep:Mapped[str]=mapped_column(CHAR(7), nullable=False)
    in_ativa:Mapped[str]=mapped_column(CHAR(1), nullable=False)
    ds_endereco:Mapped[str]=mapped_column(VARCHAR(200),nullable=False)
    cnpj:Mapped[str]=mapped_column(CHAR(14),nullable=False)
    nm_municipio:Mapped[str]=mapped_column(VARCHAR(50),nullable=False)

class Motorista(Base):
    __tablename__ = 'motorista'
    nr_matricula:Mapped[float]=mapped_column(NUMERIC(6),Sequence('TIPO_COMBUSTIVEL_SEQ'),nullable=False,primary_key=True)
    nm_motorista:Mapped[str]=mapped_column(VARCHAR(50),nullable=False)
    nr_cpf:Mapped[str]=mapped_column(VARCHAR(11),nullable=False, unique=True)
    nr_cnh:Mapped[float]=mapped_column(NUMERIC(9),nullable=False, unique=True)
    tp_categoria:Mapped[str]=mapped_column(VARCHAR(2),nullable=False)
    cd_cargo:Mapped[float]=mapped_column(NUMERIC(3), ForeignKey(CargoMotorista.cd_cargo), nullable=False)
    id_pessoa:Mapped[float]=mapped_column(NUMERIC(7,2), ForeignKey(Pessoa.id_pessoa), nullable=False)
    dt_admissao:Mapped[date]=mapped_column(Date, nullable=False)
    dt_desligamento:Mapped[date]=mapped_column(Date)
    in_ativo:Mapped[str]=mapped_column(CHAR(1),nullable=False)

class PostoConvenido(Base):
    __tablename__ = 'posto_conveniado'
    cd_posto:Mapped[float]=mapped_column(NUMERIC(6),Sequence('POSTO_CONVENIADO_SEQ'),nullable=False, primary_key=True, unique=True)
    id_pessoa:Mapped[float]=mapped_column(NUMERIC(7,2), ForeignKey(Pessoa.id_pessoa), nullable=False)
    nm_posto:Mapped[str]=mapped_column(VARCHAR(50),nullable=False)
    cnpj:Mapped[str]=mapped_column(VARCHAR(14),nullable=False, unique=True)
    dt_convenio:Mapped[date]=mapped_column(Date,nullable=False)

class UnidadeVeiculo(Base):
    __tablename__ = 'unidade_veiculo'
    id_veiculo:Mapped[float]=mapped_column(NUMERIC(7),nullable=False,primary_key=True,unique=True)
    cd_unidade:Mapped[float]=mapped_column(NUMERIC(6), ForeignKey(Unidade.cd_unidade), nullable=False)
    dt_vinculo:Mapped[date]=mapped_column(Date, nullable=False)
    dt_desvinculo:Mapped[date]=mapped_column(Date)

class Veiculo(Base):
    __tablename__ = 'veiculo'
    id_veiculo:Mapped[float]=mapped_column(NUMERIC(7), Sequence('VEICULO_SEQ'),nullable=False, primary_key=True,unique=True)
    nr_placa:Mapped[str]=mapped_column(CHAR(7),nullable=False, unique=True)
    dt_aquisicao:Mapped[date]=mapped_column(Date, nullable=False)
    dt_baixa:Mapped[date]=mapped_column(Date)
    qt_capacidadetanque:Mapped[int]=mapped_column(INTEGER, nullable=False)
    in_ativo:Mapped[str]=mapped_column(CHAR(1),nullable=False)
    cd_unidade:Mapped[float]=mapped_column(NUMERIC(6), ForeignKey(Unidade.cd_unidade), nullable=False)
    cd_tipoveiculo:Mapped[float]=mapped_column(NUMERIC(3), ForeignKey(TipoVeiculo.cd_tipoveiculo), nullable=False)
    cd_tipocombustivel:Mapped[float]=mapped_column(NUMERIC(3), ForeignKey(TipoCombustivel.cd_tipocombustivel), nullable=False)


class VeiculoMotorista(Base):
    __tablename__ = 'veiculo_motorista'
    id_veiculo:Mapped[float]=mapped_column(NUMERIC(7),nullable=False,primary_key=True, unique=True)
    cd_motorista:Mapped[float]=mapped_column(NUMERIC(6), ForeignKey(Motorista.nr_matricula), nullable=False)
    dt_vinculo:Mapped[date]=mapped_column(Date,nullable=False)
    dt_desvinculo:Mapped[date]=mapped_column(Date)


class Abastecimento(Base):
    __tablename__ = 'abastecimento'
    id_veiculo:Mapped[int]=mapped_column(INTEGER, ForeignKey(Veiculo.id_veiculo),nullable=False )
    cd_motorista:Mapped [float]=mapped_column(NUMERIC(6),ForeignKey(Motorista.nr_matricula), nullable=False)
    cd_posto:Mapped[float]=mapped_column(NUMERIC(6),ForeignKey(PostoConvenido.cd_posto), nullable=False)
    cd_tipocombustivel:Mapped[float]=mapped_column(NUMERIC(3),ForeignKey(TipoCombustivel.cd_tipocombustivel),nullable=False)
    nr_reqastecimento:Mapped[int]=mapped_column(INTEGER,nullable=False, primary_key=True)
    nr_hodometro:Mapped[float]=mapped_column(NUMERIC(7),nullable=False)
    dt_abastecimento:Mapped[datetime]=mapped_column(Date, nullable=False)  
    qt_litros:Mapped[float]=mapped_column(NUMERIC(5,2), nullable=False)
    vl_combustivel:Mapped[float]=mapped_column(NUMERIC(5,2), nullable=False)


Base.metadata.create_all(engine)

def cadastrar_pessoa(session, nm_pessoa, nr_cpfcnpj, nr_cep, ds_endereco):
    pessoa = Pessoa(
        nm_pessoa=nm_pessoa,
        nr_cpfcnpj=nr_cpfcnpj,
        nr_cep=nr_cep,
        ds_endereco=ds_endereco
    )
    session.add(pessoa)
    session.commit()

def cadastrar_tipo_combustivel(session, ds_tipocombustivel):
    tipo_combustivel = TipoCombustivel(
        ds_tipocombustivel=ds_tipocombustivel
    )
    session.add(tipo_combustivel)

# Implemente funções semelhantes para cada classe restante

# Exemplo de uso das funções de cadastro
# Supondo que você já tenha uma sessão criada e pronta para uso
# session = ...

cadastrar_pessoa(session, 'João da Silva', '12345678901', '12345678', 'Rua ABC, 123')
cadastrar_tipo_combustivel(session, 'Gasolina')
# Chame as demais funções para cadastrar instâncias das outras classes

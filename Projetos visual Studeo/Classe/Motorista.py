from datetime import *
from urllib.parse import quote
from sqlalchemy import create_engine, text
from sqlalchemy.orm import scoped_session, sessionmaker, declarative_base, Session, mapped_column, Mapped
from sqlalchemy import INTEGER, VARCHAR, CHAR, Date, NUMERIC, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.schema import Sequence
from ConectBD.ConexaoBancoDeDados import Base
from Pessoa import Pessoa
from CargoMotorista import CargoMotorista 


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

    def cad_motorista():
        pass
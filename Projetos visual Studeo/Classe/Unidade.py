from datetime import *
from urllib.parse import quote
from sqlalchemy import create_engine, text
from sqlalchemy.orm import scoped_session, sessionmaker, declarative_base, Session, mapped_column, Mapped
from sqlalchemy import INTEGER, VARCHAR, CHAR, DATE, NUMERIC, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.schema import Sequence
from Pessoa import Pessoa
from ConectBD.ConexaoBancoDeDados import Base


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

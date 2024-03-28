from datetime import *
from urllib.parse import quote
from sqlalchemy import create_engine, text
from sqlalchemy.orm import scoped_session, sessionmaker, declarative_base, Session, mapped_column, Mapped
from sqlalchemy import INTEGER, VARCHAR, CHAR, DATE, NUMERIC, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.schema import Sequence
from ConectBD.ConexaoBancoDeDados import Base


class Pessoa(Base):
    __tablename__ = 'pessoa'
    id_pessoa:Mapped[float]=mapped_column(NUMERIC(7,2),Sequence('PESSOA_SEQ'), nullable=False, primary_key=True, unique=True)
    nm_pessoa:Mapped[str]=mapped_column(VARCHAR(100), nullable=False)
    nr_cpfcnpj:Mapped[str]=mapped_column(CHAR(14), nullable=False,unique=True)
    nr_cep:Mapped[str]=mapped_column(CHAR(8), nullable=False)
    ds_endereco:Mapped[str]=mapped_column(VARCHAR(200), nullable=False)
  


def cadastrar_pessoa(self, session, nm_pessoa, nr_cpfcnpj, nr_cep, ds_endereco):
    pessoa = Pessoa(
        nm_pessoa=nm_pessoa,
        nr_cpfcnpj=nr_cpfcnpj,
        nr_cep=nr_cep,
        ds_endereco=ds_endereco
    )
    Session.add(pessoa)
    Session.commit()
    return pessoa
    
    # def ConsultaPessoa(self):
    #     for pes in self.listaPesoa:
    #         print(pes.id_pessoa, pes.nm_pessoa)

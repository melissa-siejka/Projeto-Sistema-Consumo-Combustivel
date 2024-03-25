from sqlalchemy.orm import declarative_base, mapped_column, Mapped
from sqlalchemy import INTEGER, VARCHAR, CHAR, DATE, NUMERIC, ForeignKey
from datetime import date
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






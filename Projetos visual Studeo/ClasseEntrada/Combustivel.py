from datetime import *
from urllib.parse import quote
from sqlalchemy import create_engine, text
from sqlalchemy.orm import scoped_session, sessionmaker, declarative_base, Session, mapped_column, Mapped
from sqlalchemy import INTEGER, VARCHAR, CHAR, DATE, NUMERIC, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.schema import Sequence
from Pessoa import Pessoa
from ConectBD.ConexaoBancoDeDados import Base

    
class TipoCombustivel(Base):
    __tablename__ = 'tipo_combustivel'
    cd_tipocombustivel:Mapped[float]=mapped_column(NUMERIC(3),Sequence('TIPO_COMBUSTIVEL_SEQ'),primary_key=True, nullable=False)
    ds_tipocombustivel:Mapped[str]=mapped_column(VARCHAR(50), nullable=False)

from datetime import date
from datetime import *
from urllib.parse import quote
from sqlalchemy import create_engine, text
from sqlalchemy.orm import scoped_session, sessionmaker, declarative_base, Session, mapped_column, Mapped
from sqlalchemy import INTEGER, VARCHAR, CHAR, Date, NUMERIC, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.schema import Sequence
from ConectBD.ConexaoBancoDeDados import Base
from Unidade import Unidade


class UnidadeVeiculo(Base):
    __tablename__ = 'unidade_veiculo'
    id_veiculo:Mapped[float]=mapped_column(NUMERIC(7),nullable=False,primary_key=True,unique=True)
    cd_unidade:Mapped[float]=mapped_column(NUMERIC(6), ForeignKey(Unidade.cd_unidade), nullable=False)
    dt_vinculo:Mapped[date]=mapped_column(Date, nullable=False)
    dt_desvinculo:Mapped[date]=mapped_column(Date)
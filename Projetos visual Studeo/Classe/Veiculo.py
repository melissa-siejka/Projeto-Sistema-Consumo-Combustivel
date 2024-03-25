
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
from TipoVeiculo import TipoVeiculo
from Combustivel import TipoCombustivel


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


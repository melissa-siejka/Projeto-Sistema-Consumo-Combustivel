from datetime import *
from urllib.parse import quote
from sqlalchemy import create_engine, text
from sqlalchemy.orm import scoped_session, sessionmaker,declarative_base, Session, mapped_column, Mapped
from sqlalchemy import INTEGER, VARCHAR, CHAR, DATE, NUMERIC, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.schema import Sequence
from Combustivel import TipoCombustivel
from PostoConveniado import PostoConvenido
from ConectBD.ConexaoBancoDeDados import Base
import Motorista



class Abastecimento(Base):
    __tablename__ = 'abastecimento'
    nr_reqastecimento:Mapped[int]=mapped_column(INTEGER,nullable=False, primary_key=True)
    id_veiculo:Mapped[int]=mapped_column(INTEGER, Sequence('ABASTECIMENTO_SEQ'),nullable=False )
    dt_abastecimento:Mapped[date]=mapped_column(Date, nullable=False) 
    cd_motorista:Mapped [float]=mapped_column(NUMERIC(6),ForeignKey(Motorista.nr_matricula), nullable=False)
    cd_tipocombustivel:Mapped[float]=mapped_column(NUMERIC(3),ForeignKey(TipoCombustivel.cd_tipocombustivel),nullable=False)
    cd_posto:Mapped[float]=mapped_column(NUMERIC(6),ForeignKey(PostoConvenido.cd_posto), nullable=False)
    nr_hodometro:Mapped[float]=mapped_column(NUMERIC(7),nullable=False) 
    qt_litros:Mapped[float]=mapped_column(NUMERIC(5,2), nullable=False)
    vl_combustivel:Mapped[float]=mapped_column(NUMERIC(5,2), nullable=False)




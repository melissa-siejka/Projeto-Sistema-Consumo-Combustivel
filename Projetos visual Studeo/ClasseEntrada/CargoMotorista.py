from sqlalchemy.orm import declarative_base, mapped_column, Mapped
from sqlalchemy import INTEGER, VARCHAR, CHAR, DATE, NUMERIC, ForeignKey
from datetime import date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.schema import Sequence
from ConectBD.ConexaoBancoDeDados import Base


class CargoMotorista(Base):
    __tablename__ = "cargo_motorista"
    cd_cargo:Mapped[float]=mapped_column(NUMERIC(3),Sequence('CARGO_MOTORISTA_SEQ'),nullable=False, primary_key=True)
    ds_cargo:Mapped[str]=mapped_column(VARCHAR(50))


def CadastrarCargo(session, ds_cargo):
    cargo = CargoMotorista(
        ds_cargo = ds_cargo
    )
    session.add(cargo)
    session.commit()
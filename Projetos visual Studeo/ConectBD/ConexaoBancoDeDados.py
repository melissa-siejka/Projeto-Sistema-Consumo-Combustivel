
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


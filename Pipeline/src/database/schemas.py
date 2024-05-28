from sqlalchemy import Column, TIMESTAMP, Float, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base

Base = declarative_base()
''' Classe Modelo base 'SQLAlchemy' para criação da Classe de entidade '''

class Signal(Base):
    '''  
     Classe entidade, Utilizada para armazenar dados dos sinais.

     :param id: Indentificador unico do sinal.
     :param name: Nome / legenda do sinal.
     :example: mean / max / min
    '''
    __tablename__ = 'signal'
    id = Column(Integer, primary_key=True, nullable=False, unique=True, autoincrement=True)
    name = Column(String, nullable=False)

class Data(Base):
    '''  
     Classe entidade, Utilizada para armazenar valores dos sinais.

     :param signal_id: Indentificador unico do sinal, conectado ao id da tabela 'signal'.
     :param timestamp: Data e hora de regimento do valor.
     :param value: Valor do sinal (resultado final do calculo)
    '''
    __tablename__ = 'data'
    signal_id = Column(Integer, ForeignKey('signal.id'), primary_key=True, nullable=False, unique=True, autoincrement=True)
    timestamp = Column(TIMESTAMP, nullable=False)
    value = Column(Float, nullable=False)

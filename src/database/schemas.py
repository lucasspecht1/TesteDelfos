from sqlalchemy import Column, TIMESTAMP, Float
from sqlalchemy.orm import declarative_base

Base = declarative_base()
''' Classe Modelo base 'SQLAlchemy' para criação da Classe de entidade '''

class Data(Base):
    '''  
     Classe entidade, Utilizada para armazenar dados de geração e variaveis do ambiente externo.
     :param Timestamp: Timestamp da leitura do dado.
     :param wind_speed: Velocidade do vento no ambiente.
     :param power: Potencia de geração.
     :param ambient_temperature: Temperatura ambiente externo.
    '''
    __tablename__ = "data"
    timestamp = Column(TIMESTAMP, primary_key=True, nullable=False, unique=True)
    wind_speed = Column(Float)
    power = Column(Float)
    ambient_temperature = Column(Float)
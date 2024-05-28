from src.database.schemas import Data, Signal

import os
import logging
from logging.config import fileConfig

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

''' Inicialização do arquivo de log '''
fileConfig('/Pipeline/logging_config.ini') 

logger = logging.getLogger('DATABASE')
''' Instancia de logging, salva os eventos no arquivo de log '''

class Queries:
    ''' Classe para realizar as operações de consulta ao banco de dados '''

    @staticmethod
    def __connect() -> Session:
        ''' Retorna uma conexão com o banco de dados utilizando uma instancia de 'Session' 

        :return Retorna uma instância de 'Session'
        '''
        engine = create_engine(os.getenv('DATABASE_URL'))
        
        return sessionmaker(bind=engine)()

    @staticmethod
    def __insert_data(dados: dict) -> None:
        ''' 
        Insere dados na tabela 'data', 
        o parametro 'dados' deve conter os atributos 'timestamp' e 'value'
        
        :param dados: Dicionário contendo os dados a serem inseridos
        :example: {'timestamp': '2024-05-01 00:00:00', 'value' : 1 }
        '''
        try:
            sessao = Queries.__connect()
            sessao.add(Data(timestamp=dados['timestamp'], value=dados['value']))

            sessao.commit()
            sessao.close()

        except Exception as e:
            logger.error(e)
            
    @staticmethod
    def __insert_signal(dados: dict) -> None:
        ''' 
        Insere dados na tabela 'signal', 
        o parametro 'dados' deve conter somente o atributo 'name'
        
        :param dados: Dicionário contendo os dados a serem inseridos
        :example: {'name': 'mean'}
        ''' 
        try:
            sessao = Queries.__connect()
            sessao.add(Signal(name=dados['name']))

            sessao.commit()
            sessao.close()

        except Exception as e:
            logger.error(e)

    @staticmethod
    def insertData(dados: dict) -> None:
        ''' 
        Insere dados nas tabelas 'data' e 'signal', 
        o parametro 'dados' deve conter os atributos 'timestamp', 'name' e 'value'
        insere os em ordem e de forma a conectar os dados entre as tabelas
        
        :param dados: Dicionário contendo os dados a serem inseridos
        :example: {'timestamp': '2024-05-01 00:00:00', 'name': 'mean', 'value' : 1 }
        ''' 
        Queries.__insert_signal(dados)
        Queries.__insert_data(dados)

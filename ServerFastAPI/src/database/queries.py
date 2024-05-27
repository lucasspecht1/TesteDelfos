from .schemas import Data
from const import COLUNAS

import os
from datetime import datetime
from dotenv import load_dotenv; load_dotenv()

import logging
from logging.config import fileConfig

from sqlalchemy import Column
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

''' Inicialização do arquivo de log '''
fileConfig('/ServerFastAPI/logging_config.ini') 

logger = logging.getLogger('DATABASE')
''' Instancia de logging, salva os eventos no arquivo de log '''

class Queries:
    ''' Classe para realizar as operações de consulta ao banco de dados 
    
    :method get_data_by_period: Retorna os dados no perido entre duas datas.
    :method get_data_by_timestamp: Retorna apenas o dado especificado pelo timestamp.
    '''

    __ENGINE = create_engine(os.getenv('DATABASE_URL'))
    __SESSION = sessionmaker(bind=__ENGINE)()
    ''' Instancia da sessão com a base de dados, utilizado para executar comandos SQL '''

    @staticmethod
    def __get_columns(colunas: list) -> list[Column] |  None:
        ''' Converte e retorna uma lista com os objetos Column da classe Data

        :param colunas: Lista de colunas que serão convertidas
        :example: colunas = ['timestamp', 'power']

        :return: Retorna uma lista de objetos Column da classe Data
        '''
        try:
            print(colunas)
            if len(colunas) == 0:
                logger.error('Foi informado uma lista de colunas vazia. Por favor informe ao menos uma coluna, ou remova a lista de colunas')

                return None
                
            return [getattr(Data, coluna) for coluna in colunas]

        except Exception as e:
            logger.error(e)

            return None

    @staticmethod
    def get_data_by_period(datetime_inicial: str | datetime, datetime_final: str | datetime, colunas: list = COLUNAS) -> list[Data] | None:
        '''
        Função para retornar os dados no periodo entre duas datas.

        :param data_inicial: Data inicial do periodo.
        :param data_final: Data final do periodo.
        :param colunas: Lista de colunas que deseja retornar. Por padrão retorna todas as colunas.
        :example: colunas = ['timestamp', 'power']
        
        :return: Retorna uma lista de dicionários com as colunas informadas ou None caso nenhum valor seja encontrado.
        '''
        try: 
            colunas_entidade: list[Column] = Queries.__get_columns(colunas)
            resultado: list[Data] = Queries.__SESSION.query(Data).filter(Data.timestamp.between(datetime_inicial, datetime_final)
                                                                        ).with_entities(*colunas_entidade).all()
            Queries.__SESSION.close()

            resposta = None if len(resultado) == 0 else \
                [{ coluna: getattr(item, coluna) for coluna in colunas } for item in resultado]
            
            ''' Comprehension para retornar uma lista de dicionários 
                com as colunas informadas e seus respectivos valores '''
 
            return resposta
        
        except Exception as e:
            logger.error(e)

            return None

    @staticmethod
    def get_data_by_timestamp(datetime: str | datetime, colunas: list = COLUNAS) -> Data | None:
        '''
        Função para retornar apenas o dado especificao pelo timestamp.

        :param datetime: datetime (timestamp) do dado a ser retornado.
        :example: datetime = '2024-05-01 00:00:00'
        :param colunas: Lista de colunas que deseja retornar. Por padrão retorna todas as colunas.
        :example: colunas = ['timestamp', 'power']
        
        :return: Retorna o dado ou None caso o valor não seja encontrado.
        '''
        try: 
            colunas_entidade: list[Column] = Queries.__get_columns(colunas)
            resultado: Data = Queries.__SESSION.query(Data).filter(Data.timestamp == str(datetime)
                                                                  ).with_entities(*colunas_entidade).all()

            Queries.__SESSION.close()

            resposta = None if len(resultado) == 0 else \
                 { coluna: getattr(resultado[0], coluna) for coluna in colunas } 
            
            ''' Comprehension para retornar um dicionário com as colunas 
                informadas e seus respectivos valores '''

            return resposta
            
        except Exception as e:
            logger.error(e)

            return None

    def get_last_data(colunas: list = COLUNAS) -> Data | None:
        '''
        Função para retornar apenas o dado especificao pelo timestamp.

        :param datetime: datetime (timestamp) do dado a ser retornado.
        :example: datetime = '2024-05-01 00:00:00'
        :param colunas: Lista de colunas que deseja retornar. Por padrão retorna todas as colunas.
        :example: colunas = ['timestamp', 'power']
        
        :return: Retorna o dado ou None caso o valor não seja encontrado.
        '''
        try:
            colunas_entidade: list[Column] = Queries.__get_columns(colunas)
            resultado: Data = Queries.__SESSION.query(Data).order_by(Data.timestamp.desc()
                                                                    ).limit(1).with_entities(*colunas_entidade).all()

            Queries.__SESSION.close()

            resposta = None if len(resultado) == 0 else \
                 { coluna: getattr(resultado[0], coluna) for coluna in colunas } 
            
            ''' Comprehension para retornar um dicionário com as colunas 
                informadas e seus respectivos valores '''
                                           
            return resposta
            
        except Exception as e:
            logger.error(e)

            return None
        
    def get_first_data(colunas: list = COLUNAS) -> Data | None:
        '''
        Função para retornar apenas o dado especificao pelo timestamp.

        :param datetime: datetime (timestamp) do dado a ser retornado.
        :example: datetime = '2024-05-01 00:00:00'
        :param colunas: Lista de colunas que deseja retornar. Por padrão retorna todas as colunas.
        :example: colunas = ['timestamp', 'power']
        
        :return: Retorna o dado ou None caso o valor não seja encontrado.
        '''
        try: 
            if colunas.__len__() == 0:
                raise Exception('Foi informado uma lista de colunas vazia. Por favor informe ao menos uma coluna, ou remova a lista de colunas')

            else:
                colunas_entidade: list[Column] = Queries.__get_columns(colunas)
                resultado_extracao: Data = Queries.__SESSION.query(Data).order_by(Data.timestamp.asc()
                                                                                 ).limit(1).with_entities(*colunas_entidade).all()

            Queries.__SESSION.close()

            if len(resultado_extracao) == 0:
                return None
            
            else: 
                ''' Comprehension para retornar uma lista de dicionários com as colunas informadas e seus respectivos valores '''
                return { coluna: getattr(resultado_extracao[0], coluna) for coluna in colunas }
            
        except Exception as e:
            logger.error(e)

            return None
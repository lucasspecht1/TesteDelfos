import numpy
from dagster import op
from typing import List, Optional

from logging.config import fileConfig
from logging import getLogger

''' Inicializa os loggers a partir de um arquivo de configuração '''
fileConfig('/Pipeline/logging_config.ini')

log_calc = getLogger('CALC')
''' Log para registro de eventos de execução'''

class Calc:
    ''' Classe responsável por executar 
     os calculos do dados de pipeline '''

    @staticmethod
    def __get_keys_calculate(dados: List[dict]) -> List:
        '''
        Retorna as chaves do dicionario excluindo o timestamp que não pode ser calculado

        :param dados: Array de dicionários contendo os dados.

        :return Retorna uma lista contendo as chaves do dicionario
        '''
        colunas = []

        for coluna in dados[0].keys():
                colunas.append(coluna) if coluna != 'timestamp' else None
        ''' Recebe todas as chaves do dicionario e transforma 
            em uma lista de colunas iteravel'''

        return colunas
    
    @staticmethod
    def __transform_list_one_dict(dados: List[dict]) -> dict:
        '''
        Transforma uma lista de dicionários em um unico dicionário

        :param dados: Array de dicionários contendo os dados.
        :example: [{'timestamp': '2024-05-01 00:00:00', 'power' : 1 }, 
                   {'timestamp': '2024-05-01 01:00:00', 'power' : 5 }]

        :return: Retorna um dicionário contendo todos os dados do array de dicionários.
        :example: {'timestamp': ['2024-05-01 00:00:00', '2024-05-01 01:00:00'], 'power' : [1, 5]}
        '''
        colunas = Calc.__get_keys_calculate(dados)

        valores = {coluna: [dado[coluna] for dado in dados] for coluna in colunas}
        ''' Comprehension para transformar os dados dos dicionarios na lista em
            um dicionario contendo todos os valores em array '''

        return valores
    
    @staticmethod
    def calculate_mean(dados: List[dict]) -> Optional[dict]:
        ''' 
        Calcula e retorna a média dos valores em um array de dicionários 

        :param dados: Array de dicionários contendo os dados.
        :example: [{'timestamp': '2024-05-01 00:00:00', 'power' : 1 }, 
                   {'timestamp': '2024-05-01 01:00:00', 'power' : 5 }]

        :return: Retorna um dicionário contendo a média dos valores ou None 
                 caso o array de dicionários seja vazio ou haja erros.
        '''
        try: 
            colunas = Calc.__get_keys_calculate(dados)
            valores = Calc.__transform_list_one_dict(dados)

            valores = {coluna: sum(valores[coluna]) / len(valores[coluna]) for coluna in colunas}
            ''' Executa o calculo de média baseando se nas colunas do dicionário, 
                e alterna seu valor para resultado do calculo '''

            return valores

        except Exception as e:
            log_calc.error(e)

            return None

    @staticmethod
    def calculate_min(dados: List[dict]) -> Optional[dict]:
        ''' 
        Calcula e retorna a minima dos valores em um array de dicionários 

        :param dados: Array de dicionários contendo os dados.
        :example: [{'timestamp': '2024-05-01 00:00:00', 'power' : 1 }, 
                   {'timestamp': '2024-05-01 01:00:00', 'power' : 5 }]

        :return: Retorna um dicionário contendo a média dos valores ou None 
                 caso o array de dicionários seja vazio ou haja erros.
        '''
        try: 
            colunas = Calc.__get_keys_calculate(dados)
            valores = Calc.__transform_list_one_dict(dados)

            valores = {coluna: min(valores[coluna]) for coluna in colunas}
            ''' Executa o calculo de minima baseando se nas colunas do dicionário, 
                e alterna seu valor para resultado do calculo '''

            return valores

        except Exception as e:
            log_calc.error(e)

            return None

    @staticmethod
    def calculate_max(dados: List[dict]) -> Optional[dict]:
        ''' 
        Calcula e retorna a maxima dos valores em um array de dicionários 

        :param dados: Array de dicionários contendo os dados.
        :example: [{'timestamp': '2024-05-01 00:00:00', 'power' : 1 }, 
                   {'timestamp': '2024-05-01 01:00:00', 'power' : 5 }]

        :return: Retorna um dicionário contendo a média dos valores ou None 
                 caso o array de dicionários seja vazio ou haja erros.
        '''
        try: 
            colunas = Calc.__get_keys_calculate(dados)
            valores = Calc.__transform_list_one_dict(dados)

            valores = {coluna: max(valores[coluna]) for coluna in colunas}
            ''' Executa o calculo de maxima baseando se nas colunas do dicionário, 
                e alterna seu valor para resultado do calculo '''

            return valores

        except Exception as e:
            log_calc.error(e)

            return None
    
    @staticmethod
    def calculate_standard_deviation(dados: List[dict]) -> Optional[dict]:
        ''' 
        Calcula e retorna o desvio padrão dos valores em um array de dicionários 

        :param dados: Array de dicionários contendo os dados.
        :example: [{'timestamp': '2024-05-01 00:00:00', 'power' : 1 }, 
                   {'timestamp': '2024-05-01 01:00:00', 'power' : 5 }]

        :return: Retorna um dicionário contendo o desvio padrão dos valores ou None 
                 caso o array de dicionários seja vazio ou haja erros.
        '''
        try: 
            colunas = Calc.__get_keys_calculate(dados)
            valores = Calc.__transform_list_one_dict(dados)

            valores = {coluna: numpy.std(valores[coluna]) for coluna in colunas}
            ''' Executa o calculo de maxima baseando se nas colunas do dicionário, 
                e alterna seu valor para resultado do calculo '''

            return valores

        except Exception as e:
            log_calc.error(e)

            return None
import httpx

from datetime import datetime, timedelta
from dagster import asset, op, job

from logging.config import fileConfig
from logging import getLogger

from const import COLUNAS
from calc import Calc

fileConfig(r'logging_config.ini')
log_api = getLogger('API')
log_calc = getLogger('CALC')

class Pipeline:

    @asset
    @staticmethod
    def get_data_by_day(dia: str, colunas: list = COLUNAS)-> list[dict] | None:
        ''' 
        Retorna os dados do dia inteiro informado

        :param dia: Data no formato YYYY-MM-DD 
        :example: '2024-05-03'
        :param colunas - Opcional: Lista de colunas que deseja retornar
        :example: ['timestamp', 'power']

        :return: Retorna uma lista de Dicionários com os dados do dia informado Caso o periodo exista ou None caso o dia informado nao exista
        '''
        try:
            inicio_periodo = datetime.strptime(dia, '%Y-%m-%d').date()
            fim_periodo = inicio_periodo + timedelta(days=1)

            return httpx.get('http://localhost:8000/database/get/by/period', params={ 'start': inicio_periodo, 
                                                                                      'colunas': colunas,
                                                                                      'end': fim_periodo }).json()  
        
        except Exception as e:
            log_api.error(e)

            return None

    @op
    @staticmethod
    def separate_10mins(dados: list[dict]) -> list[dict]:
        resultado = []

        bloco = []

        for dado in dados:
            bloco.append(dado)

            if datetime.strptime(dado['timestamp'], '%Y-%m-%dT%H:%M:%S').minute % 10 == 0:
                resultado.append(bloco)
                bloco = []

        print(resultado)

    @staticmethod
    def process_day(dia: str, colunas: list = COLUNAS):
        resultado = Pipeline.get_data_by_day(dia)

        if resultado is not None:
            return Calc.calculate_mean(resultado)
        
        else:
            return None

data = Pipeline.get_data_by_day('2024-05-01', colunas=['timestamp', 'power', 'wind_speed', 'ambient_temperature'])
print(Pipeline.separate_10mins(data))
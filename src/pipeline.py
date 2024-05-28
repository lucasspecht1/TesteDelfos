import httpx
from typing import List, Dict, Optional

from datetime import datetime, timedelta
from dagster import op, job, Out
from dotenv import load_dotenv; load_dotenv()

from logging.config import fileConfig
from logging import getLogger

from src.database.queries import Queries
from const import COLUNAS
from src.calc import Calc

''' Inicialização do arquivo de log '''
fileConfig('/Pipeline/logging_config.ini')

''' Instancias de logging, salva os eventos no arquivo de log '''
log_api = getLogger('API')
log_op = getLogger('OP')

@op(out=Out(List[dict], is_required=False))
def get_data_by_day(dia: str, colunas: List = COLUNAS)-> Optional[List[dict]]:
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

        return httpx.get('http://server-fastapi:8000/database/get/by/period', params={ 'start': inicio_periodo, 'colunas': colunas, 'end': fim_periodo }).json()  
        
    except Exception as e:
        log_api.error(e)

        return None
    
@op
def separate_10mins(dados: List[dict]) -> Optional[List[List[dict]]]:
    ''' 
    Retorna os dados separados em blocos de 10 minutos.

    :param dados: Array de dicionários contendo os dados.
    :return: Retorna uma lista de dicionários contendo os dados separados em blocos de 10 minutos
    '''
    try:
        resultado = []
        bloco = []

        for index, dado in enumerate(dados):
            bloco.append(dado)

            minute = datetime.strptime(dado['timestamp'], '%Y-%m-%dT%H:%M:%S').minute
            ''' Minuto do horário em que o dado foi coletado '''

            if minute % 10 == 0 and index != 0:
                ''' define blocos de 10 em 10 minutos '''
                resultado.append(bloco)
                bloco = []

        return resultado
        
    except Exception as e:
        log_op.error(e)

        return None

@op
def process_values(timestamp: str, name: str, dados: dict)-> None:
    '''
    Processa e envia o dado a base de dados 'alvo' com sua nomenclatura e valor correspondente

    :param timestamp: Timestamp de regimento do dado.
    :example: '2024-05-01 00:00:00'
    :param name: nomenclatura do dado.
    :example: 'mean' | 'min'
    :param dados: Dicionário contendo os dados.
    :example: {'timestamp': '2024-05-01 00:00:00', 'power' : 1 }
    '''
    try:
        for coluna in list(dados.keys()):
            Queries.insertData({'timestamp' : timestamp, 
                                     'name' : f'{name}_{coluna}', 
                                    'value' : dados[coluna]})

    except Exception as e:
        log_op.error(e)

@op
def process_blocks(blocos: List[List[dict]]) -> None:
    ''' 
    Processa os blocos de dados e calcula as metricas de cada bloco, 
    após isso envia esses dados para a base de dados 'alvo'.
    
    :param blocos: Blocos de dados a serem processados
    :example: [[{'timestamp' : '2024-05-01', 'power': '1'}]]
    '''
    for bloco in blocos:
        timestamp = datetime.strptime(bloco[-1]['timestamp'], '%Y-%m-%dT%H:%M:%S').strftime('%Y-%m-%d %H:%M:%S')

        process_values(timestamp, 'mean', Calc.calculate_mean(bloco))
        process_values(timestamp, 'min', Calc.calculate_min(bloco))
        process_values(timestamp, 'max', Calc.calculate_max(bloco))
        process_values(timestamp, 'standard_deviation', Calc.calculate_standard_deviation(bloco))

@job
def run(timestamp: str = '2024-05-01')-> None:
    ''' 
    Método principal para execução da linha de tratameto de dados,
    inicia o tratamento dos dados do dia informado e executa o por meio de uma Pipeline.
    
    :param timestamp: Timestamp do dia que deseja processar
    :example: '2024-05-05'
    :default: '2024-05-01'
    '''
    data = get_data_by_day(timestamp)
    if data:
        blocos = separate_10mins(data)
        if blocos:
            process_blocks(blocos)
    

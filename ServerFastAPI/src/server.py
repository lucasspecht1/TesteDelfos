from const import COLUNAS
from .database.queries import Queries

from typing import List
from datetime import datetime
from fastapi import APIRouter, Query

router = APIRouter()

@router.get("/get/last")
def return_last(colunas: List[str] = Query(COLUNAS)) -> dict | None:
    """
    Rota para retornar o dado mais recente (ultima ocorência) na base de dados.

    :param colunas - opcional: Lista de colunas que deseja retornar. Por padrão retorna todas as colunas.
    :example: colunas = ['timestamp', 'power']

    :return: dict | None: o dado lido como um dicionário, ou None se nenhum dado for encontrado.
    """
    return Queries.get_last_data(colunas)

@router.get("/get/first")
def return_first(colunas: List[str] = Query(COLUNAS)) -> dict | None:
    """
    Rota para retornar o dado mais antigo (primeira ocorência) na base de dados.

    :param colunas - opcional: Lista de colunas que deseja retornar. Por padrão retorna todas as colunas.
    :example: colunas = ['timestamp', 'power']

    :return: dict | None: o dado lido como um dicionário, ou None se nenhum dado for encontrado.
    """
    return Queries.get_first_data(colunas)
    
@router.get("/get/by/datetime")
def return_by_timestamp(datetime: datetime, colunas: List[str] = Query(COLUNAS)) -> dict | None:
    """
    Rota para retornar o dado especifico (definido pelo parametro 'datetime').
    
    :param datetime: datetime (timestamp) do dado a ser retornado.
    :example: datetime = '2024-05-01 00:00:00'
    :param colunas: Lista de colunas que deseja retornar. Por padrão retorna todas as colunas.
    :example: colunas = ['timestamp', 'power']

    :return: dict | None: o dado lido como um dicionário, ou None se nenhum dado for encontrado.
    """
    return Queries.get_data_by_timestamp(datetime, colunas)

@router.get("/get/by/period")
def return_by_period(start: datetime, end: datetime, colunas: List[str] = Query(COLUNAS)) -> list[dict] | None:
    """
    Rota para retornar os dados dentro do periodo (definido pelo parametros 'start' e 'end').
    
    :param start: datetime (timestamp) do inicio do periodo.
    :param end: datetime (timestamp) do fim do periodo.
    :param colunas: Lista de colunas que deseja retornar. Por padrão retorna todas as colunas.
    :example: colunas = ['timestamp', 'power']

    :return: dict | None: o dado lido como um dicionário, ou None se nenhum dado for encontrado.
    """
    return Queries.get_data_by_period(start, end, colunas)

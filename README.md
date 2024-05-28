[![My Skills](https://skillicons.dev/icons?i=python)](https://skillicons.dev) [Pipeline ETL](https://github.com/lucasspecht1/Teste_Data_Eng/tree/Pipeline)
------------------

Infos:
  - Porta Externa: 3000
  - Pasta Script: `/Pipeline`

_Este container contendo o módulo de Pipeline ETL possui a tag `pipeline`,_
_construido utilizando `Dagster`, inicia de forma automatica o servidor Dagster._

Existem duas formas de executar o script de ETL:

**1º Forma**
------------
_Utilizando o serviço Dagster, executando o 'job' run com o parametro de dia desejado da seguinte forma: `{'inputs': {'timestamp': '2024-05-05'}}`_
_desta forma o Dagster irá executar o método principal da ETL, executando todo o processo necessario, até a inserção no Banco de dados 'alvo'_

**2º Forma**
------------
_Executando diretamente o script python, dentro da pasta `/Pipeline` _
_temos um arquivo chamado `main.py` este arquivo será utilizado para executar o Script_
_para isso deveremos rodar o seguinte comando: `python3 /Pipeline/main.py -t <dia_escolhido>`, _
_onde o script sera executado com o argumento do dia a ser processado, utilizamos `-t ou --timestamp` seguido do dia no formato: `yyyy-mm-dd`_
_caso nenhum dia sejá informado o dia padrão é o primeiro: (2024-05-01)_

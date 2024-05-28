Este repositório é destinado ao versionamento do teste prático - Delfos

Teste Prático Delfos
====================

 _Esta documentação será divida em categorias destinadas a cada aplicação / container docker_

🖥️ Informações importantes
--------------------------

- Para rodar os containers basta executar `docker compose up`.
- Todos os containers estarão previamente configurados para execução.

[![My Skills](https://skillicons.dev/icons?i=postgresql)](https://skillicons.dev) [Banco de dados Fonte](https://github.com/lucasspecht1/Teste_Data_Eng/tree/BancoFonte)
------------------

Infos:
  - Porta externa: 5000
  - usuario: user_fonte
  - senha: 12345

_Este container contendo o Banco de dados possui a tag `db_fonte` no docker,_
_possui dados previamente gerados aleatoriamente, todos re inseridos ao banco_
_na primeira execução de `docker compose up`_

Periodo dos dados presentes (10 dias) 2024-05-01 00:00:00 até 2024-05-10 00:00:00

Os dados estão organizados da seguinte da forma:
  - timestamp (datetime de leitura)
  - wind_speed (leitura de velocidade do vento em 'm/s')
  - power (leitura de geração em 'kw')
  - ambient_temperature (leitura de temperatura em 'ºC')

[![My Skills](https://skillicons.dev/icons?i=postgresql)](https://skillicons.dev) [Banco de dados Alvo](https://github.com/lucasspecht1/Teste_Data_Eng/tree/BancoAlvo)
------------------

Infos:
  - Porta externa: 5001
  - usuario: user_alvo
  - senha: 12345

_Este container contendo o Banco de dados possui a tag `db_alvo` no docker,_
_possui configuração preedefinada inserida na primeira execução de `docker compose up`._

[![My Skills](https://skillicons.dev/icons?i=fastapi)](https://skillicons.dev) [Server FastAPI](https://github.com/lucasspecht1/Teste_Data_Eng/tree/ServerFastAPI)
------------------

Infos:
  - Rota base: `http://localhost:8000`
  - Porta externa: 8000

_Este container contendo a API de consultas possui a tag `ServerFastAPI`,_
_executa de forma automatica o servidor `FastAPI` no momento da execução do container,_
_não há necessidade de comandos de execução ou parametros._

Periodo dos dados disponiveis (10 dias) 2024-05-01 00:00:00 até 2024-05-10 00:00:00

Rotas existentes:
  - `/database/get/first` (Retorna o primeiro dado existente no banco)
    - Parametros:
        - **opcional** - colunas: `list` Lista contendo as colunas desejadas 
                         Exemplo: ['timestamp', 'power']
 
  - `/database/get/last` (Retorna o ultimo dado inserido no banco)
    - Parametros:
        - **opcional** - colunas: `list` Lista contendo as colunas desejadas 
                         Exemplo: ['timestamp', 'power']

  - `/database/get/by/datetime` (Retorna o dado correspondente ao datetime passado no parametro)
    - Parametros:
        - datetime: `string` Data e Tempo do dado a ser coletado (no padrão americano yyyy-mm-dd HH:MM:SS)
           Exemplo: '2024-05-01 00:00:00'

        - **opcional** - colunas: Lista contendo as colunas desejadas 
                         Exemplo: ['timestamp', 'power']

  - `/database/get/by/period` (Retorna os dados correspondentes ao periodo passado no parametro)
    - Parametros:
        - start: `string` Data e Tempo do inicio do periodo de coleta (no padrão americano yyyy-mm-dd HH:MM:SS)
           Exemplo: '2024-05-01 00:00:00'

        - end: `string` Data e Tempo do fim do periodo de coleta (no padrão americano yyyy-mm-dd HH:MM:SS)
           Exemplo: '2024-05-10 00:00:00'

        - **opcional** - colunas: Lista contendo as colunas desejadas 
                         Exemplo: ['timestamp', 'power']

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
_Executando diretamente o script python, dentro da pasta `/Pipeline` 
_temos um arquivo chamado `main.py` este arquivo será utilizado para executar o Script_
_para isso deveremos rodar o seguinte comando: `python3 /Pipeline/main.py -t <dia_escolhido>`, 
_onde o script sera executado com o argumento do dia a ser processado, utilizamos `-t ou --timestamp` seguido do dia no formato: `yyyy-mm-dd`_
_caso nenhum dia sejá informado o dia padrão é o primeiro: (2024-05-01)_


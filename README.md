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
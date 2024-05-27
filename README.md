Este repositório é destinado ao versionamento do teste prático - Delfos

Teste Prático Delfos
====================

 _Esta documentação será divida em categorias destinadas a cada aplicação / container docker_

🖥️ Informações importantes
--------------------------

- Para rodar os containers basta executar `docker compose up`.
- Todos os containers estarão previamente configurados para execução.

[![My Skills](https://skillicons.dev/icons?i=postgresql)](https://skillicons.dev) Banco de dados Fonte
------------------
Infos:
  - Porta externa: 5000
  - usuario: user_fonte
  - senha: 12345

_Este container contendo o Banco de dados possui a tag `db_fonte` no docker,_
_possui dados previamente gerados aleatoriamente, todos re inseridos ao banco_
_na primeira execução de `docker compose up`, os dados estão organizados da seguinte da forma:_
  - timestamp (datetime de leitura)
  - wind_speed (leitura de velocidade do vento em 'm/s')
  - power (leitura de geração em 'kw')
  - ambient_temperature (leitura de temperatura em 'ºC')

[![My Skills](https://skillicons.dev/icons?i=postgresql)](https://skillicons.dev) Banco de dados Alvo
------------------
Infos:
  - Porta externa: 5001
  - usuario: user_alvo
  - senha: 12345

_Este container contendo o Banco de dados possui a tag `db_alvo` no docker,_
_possui configuração preedefinada inserida na prima execução de `docker compose up`._

[![My Skills](https://skillicons.dev/icons?i=fastapi)](https://skillicons.dev) Server FastAPI
------------------

[![My Skills](https://skillicons.dev/icons?i=python)](https://skillicons.dev) Script ETL
------------------

# pipeline-weather

## 📌 Sobre
Este projeto é uma **pipeline de ETL (Extração, Transformação e Carga)** que captura dados de clima em tempo real usando a **API OpenWeather**, transforma os dados e carrega em um banco **PostgreSQL**.

> 🚧 Projeto baseado no tutorial: https://github.com/vbluuiza/pipeline_etl_weather_data_tutorial_youtube

A orquestração é feita com **Apache Airflow** (via `docker-compose`), executando um DAG (`weather_pipeline`) que:

1. Extrai dados de clima para o Rio de Janeiro (OpenWeather)
2. Transforma o JSON em um `DataFrame` e normaliza campos
3. Carrega os dados em uma tabela PostgreSQL (`rj_weather`)

---

## 🚀 Como executar (modo recomendado)
### 1) Pré-requisitos
- Docker & Docker Compose (versão compatível com Airflow)
- Você deve estar em um ambiente com recurso suficiente (mínimo ~4GB RAM)

### 2) Configurar variáveis de ambiente
1) Gere sua chave da OpenWeather (API Key):
   - Acesse https://openweathermap.org/
   - Crie uma conta (ou faça login)
   - Vá em “API keys” no painel e gere uma nova chave

2) Crie um arquivo `config/.env` com as variáveis abaixo (substitua pelos seus valores):

```env
# Chave da API OpenWeather
OPENWEATHER_API_KEY="<SUA_OPENWEATHER_API_KEY_AQUI>"

# Conexão com o banco de dados onde os dados serão carregados
database="wheather_data"
user="wheater_user"
password="<SUA_SENHA_AQUI>"
```

> **Atenção:** não comite chaves/credenciais reais no repositório; mantenha o `.env` fora do versionamento.

### 3) Iniciar o Airflow (via Docker)
No diretório raiz do projeto:

```bash
docker compose up --build
```

Isso iniciará os serviços do Airflow, Redis e PostgreSQL.

### 4) Acessar a interface do Airflow
- Web UI: http://localhost:8080
- Usuário/PWD padrão: `airflow` / `airflow`

### 5) Executar o DAG
- No Airflow UI, encontre o DAG `weather_pipeline`
- Ative-o (toggle) e acione um *Trigger Dag* ou aguarde a execução agendada (a cada hora)

---

## 🧩 Estrutura do projeto
- `dags/weather_data.py` - definição do DAG do Airflow
- `src/` - código de extração, transformação e carga
- `config/.env` - variáveis de ambiente (API key + credenciais PostgreSQL)
- `data/` - saída local (`weather_data.json`, `temp_data.parquet`)

---

## 🧪 Testar localmente (sem Airflow)
> **Observação:** o script principal (`main.py`) está comentado por padrão.

1) Crie e ative um ambiente virtual Python

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt  # ou pip install -e .
```

2) Execute o pipeline (ajuste `config/.env` com sua chave da OpenWeather API):

```bash
python main.py
```

---

## 📌 Observações
- O fluxo atual busca dados apenas para o Rio de Janeiro (`q=Rio de Janeiro,BR`). Ajuste o endpoint em `dags/weather_data.py` se quiser outra localização.
- O banco PostgreSQL usado pelo Airflow é `airflow`, mas os dados de clima são gravados em `wheather_data` (conforme `config/.env`).

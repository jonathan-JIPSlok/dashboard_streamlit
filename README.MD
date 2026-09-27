# Dashboard interativo usando Streamlit

## Passo 1: Configuração do Ambiente

- Instale o Poetry para gerenciar suas dependências python

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

## Passo 2: tabelas e views
- Conecte-se ao Clickhouse e crie a tabela e views necessárias [Comando SQL](./sql_clickhouse/tabelasAndViews.sql)

## Passo 3: adicione as dependencias
```bash
poetry add
```

## passo 4: 
- caso não use AWS S3
´´´bash
poetry run .\pipeline_semS3.py
´´´
- caso use, configure o boto3 no [Pipeline](./pipeline.py)
```bash
poetry run .\pipeline.py
```

## passo 5: abra o dashboard
´´´bash
poetry run streamlit run .\dashboard.py
´´´
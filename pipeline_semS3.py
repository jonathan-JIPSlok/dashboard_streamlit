import pandas as pd
import clickhouse_connect
from datetime import datetime
import os
from io import StringIO

# Conexão com ClickHouse
client = clickhouse_connect.get_client(
    host='localhost',
    port='8123',
    username='user',
    password='password'
)

def process_csv(file_path):
    # Ler CSV local
    df = pd.read_csv(file_path)

    # Adicionar colunas adicionais
    df['data_ingestao'] = datetime.now()
    df['data_line'] = pd.to_datetime(df['timestamp'])  # mapeia timestamp → data_line
    df['tag'] = os.path.basename(file_path)

    # Inserir dados no ClickHouse em lote
    rows = [
        (row['data_ingestao'], row['data_line'], row['tag'])
        for _, row in df.iterrows()
    ]
    client.insert(
        'data_pipeline',
        rows,
        column_names=['data_ingestao','data_line','tag']
    )

def main():
    file_path = './iot_data/iot_data.csv'
    process_csv(file_path)

if __name__ == '__main__':
    main()

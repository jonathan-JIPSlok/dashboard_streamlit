import boto3
import pandas as pd
import clickhouse_connect
from datetime import datetime
import os
import io

# Configurações do S3
s3_client = boto3.client('s3')
bucket_name = 'iot_data'
prefix = 'iot_data/iot_data.csv'

# Conexão com ClickHouse
client = clickhouse_connect.get_client(host='localhost', port='8123', username='user', password='password')

def process_csv(object_key):   
   # Baixar o arquivo CSV do S3   
    response = s3_client.get_object(
        Bucket=bucket_name,
        Key=object_key
    )    
    csv_content = response['Body'].read().decode('utf-8')    

    # Ler CSV com pandas    
    df = pd.read_csv(io.StringIO(csv_content))

    # Adicionar colunas adicionais    
    df['data_ingestao'] = datetime.now()    
    df['tag'] = os.path.basename(object_key)

    # Inserir dados no ClickHouse
    for index, row in df.iterrows():        
        client.execute(
            'INSERT INTO data_pipeline (data_ingestao, data_line, tag) VALUES',            
            [(row['data_ingestao'], row['data_line'], row['tag'])]
        )

def main():    
    # Listar arquivos no bucket S3    
    response = s3_client.list_objects_v2(
        Bucket=bucket_name,
        Prefix=prefix
    )    
    for obj in response.get('Contents', []):        
        process_csv(obj['Key'])


if __name__ == '__main__':
    main()
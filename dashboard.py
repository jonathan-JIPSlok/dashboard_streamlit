import streamlit as st
import clickhouse_connect
import pandas as pd


# Conexão com ClickHouse
client = clickhouse_connect.get_client(host='localhost', port='8123', username='user', password='password')

st.title("Dashboard de Dados IoT")

# Consulta para o resumo diário
daily_summary = client.query("SELECT * FROM daily_summary")
df_daily = pd.DataFrame(
    daily_summary.result_rows,
    columns=daily_summary.column_names)

st.subheader("Resumo Diário")
st.line_chart(df_daily.set_index('date'))

# Consulta para o resumo por tag
tag_summary = client.query("SELECT * FROM tag_summary")
df_tag = pd.DataFrame(tag_summary.result_rows,
columns=tag_summary.column_names)

st.subheader("Resumo por Tag")

st.bar_chart(df_tag.set_index('tag'))
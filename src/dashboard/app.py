import streamlit as st
import pandas as pd
import sqlite3

# Conectar a um banco de dados SQLite
connection = sqlite3.connect('../data/quotes.db')

# Carregar os dados da tabela 'mercadolivre_items' em um DataFrame pandas
dataFrame = pd.read_sql_query("SELECT * FROM mercadolivre_items",connection)

# Fechar conexão com banco de dados
connection.close()

# Definir título da aplicação
st.title("Pesquisa de Mercado - Tênis Esportivos Masculinos no Mercado Livre")

# Melhorar o layout com colunas para KPIs
st.subheader("KPIs principais do sistema")
col1, col2, col3 = st.columns(3)

# KPI 1: número total de itens
total_items = dataFrame.shape[0]
col1.metric(label="Número total de itens", value=total_items)

# KPI 2: número de marcas únicas
total_unique_brands = dataFrame['brand'].nunique()
col2.metric(label="Número de marcas únicas", value=total_unique_brands)

# KPI 3: Média de novos preços (em reais)
average_new_price = dataFrame['new_price'].mean()
col3.metric(label="Média de novos preços (R$)", value=f"{average_new_price:.2f}")

# Quais marcas são mais encontradas até a página 10?
st.subheader("Marcas mais encontradas até a página 10")
col1, col2 = st.columns([4,2])
top_brands_till_page_10 = dataFrame['brand'].value_counts().sort_values(ascending=False)
col1.bar_chart(top_brands_till_page_10)
col2.write(top_brands_till_page_10)

# Qual a média de preços por marca?
st.subheader("Média de preços por marca")
col1, col2 = st.columns([4,2])
average_price_by_brand = dataFrame.groupby('brand')['new_price'].mean().sort_values(ascending=False)
col1.bar_chart(average_price_by_brand)
col2.write(average_price_by_brand)

# Qual o nível de satisfação por marca?
st.subheader("Nível de satisfação por marca")
col1, col2 = st.columns([4,2])
dataFrame_non_zero_reviews = dataFrame[dataFrame['reviews_rating_number'] > 0]
satisfaction_by_brand = dataFrame_non_zero_reviews.groupby('brand')['reviews_rating_number'].mean().sort_values(ascending=False)
col1.bar_chart(satisfaction_by_brand)
col2.write(satisfaction_by_brand)

# st.write(dataFrame)
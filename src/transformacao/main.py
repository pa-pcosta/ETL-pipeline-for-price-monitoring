# Importar o que precisamos
import pandas as pd
from datetime import datetime
import sqlite3

# Setar pandas para mostrar todas as colunas
# pd.options.display.max_columns = None

# Definir o caminho para o arquivo de dados
dataFrame = pd.read_json('data\data.jsonl', lines=True)

# Adicionar a coluna _source com um valor fixo
dataFrame['_source'] = "https://lista.mercadolivre.com.br/tenis-corrida-masculino"

# Adicionar a coluna _extraction_date com data e hora da coleta
dataFrame['_extraction_date'] = datetime.now()

# Tratar os valores nulos para colunas numéricas e de texto
dataFrame['old_price_reais'] = dataFrame['old_price_reais'].fillna(0).astype(float)
dataFrame['old_price_centavos'] = dataFrame['old_price_centavos'].fillna(0).astype(float)
dataFrame['new_price_reais'] = dataFrame['new_price_reais'].fillna(0).astype(float)
dataFrame['new_price_centavos'] = dataFrame['new_price_centavos'].fillna(0).astype(float)
dataFrame['reviews_rating_number'] = dataFrame['reviews_rating_number'].fillna(0).astype(float)

# Remover os parênteses da coluna reviews_amount
dataFrame['reviews_amount'] = dataFrame['reviews_amount'].str.replace('[\(\)]', '', regex=True)
dataFrame['reviews_amount'] = dataFrame['reviews_amount'].fillna(0).astype(int)

# Tratar os preços como float e calcular os valores totais
dataFrame['old_price'] = dataFrame['old_price_reais'] + dataFrame['old_price_centavos'] / 100
dataFrame['new_price'] = dataFrame['new_price_reais'] + dataFrame['new_price_centavos'] / 100

# Remover antigas colunas de preços
dataFrame.drop(columns=['old_price_reais', 'old_price_centavos', 'new_price_reais', 'new_price_centavos'])

# Conectar a um banco de dados SQLite
connection = sqlite3.connect('data/quotes.db')

# Salvar o dataFrame no banco de dados
dataFrame.to_sql('mercadolivre_items', connection, if_exists='replace', index=False)

# Fechar conexão com banco de dados
connection.close()

# DEBUG imprime dataFrame
print(dataFrame.head())
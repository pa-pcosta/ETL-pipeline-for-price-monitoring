
# ETL Pipeline for Price Monitoring

## Contents

### :large_blue_circle::red_circle::white_circle: _EN-US_
- [Description](#description)
- [Objective](#objective)
- [Tools used](#tools-used)

### :green_circle::yellow_circle: _PT-BR_
- [Descrição](#descrição)
- [Objetivo](#objetivo)
- [Ferramentas Utilizadas](#ferramentas-utilizadas)

---

### :large_blue_circle::red_circle::white_circle: _EN-US_
## Description
This repository contains a data analysis for a ficticious company that would like a **market research** in the category of _male sports sneakears_ on the web page _Mercado Livre_ to analyze the following points:

1. What are the brands wich appear the most on the 10 first pages?
2. How much is the average price by brand?
3. What is the average satisfaction by brand?

## Objective
This project was developed to apply data engenieering concepts (specially data ETL pipeline), through **web scraping** technique, using modern tools.

## Tools used
(Extraction)
- Web Scraping
- Scrapy
(Transformation)
- Python
- Pandas
(Loading and visualization)
- Streamlit

---

### :green_circle::yellow_circle: _PT-BR_
## Descrição
Este repositório contém um projeto de análise de dados de uma empresa fictícia que deseja fazer uma **pesquisa de mercado** na categoria _tênis esportivos masculinos_ na página _Mercado Livre_ para avaliar a concorrência nos seguintes pontos:

1. Quais marcas são mais encontradas nas 10 primeiras páginas?
2. Qual o preço médio por marca?
3. Qual a média de satisfação por marca?

## Objetivo
Este projeto foi desenvolvido para aplicar conceitos de engenharia de dados (mais especificamente o processo de ETL de dados), através da técnica de **web scraping**, utilizando ferramentas modernas.

## Ferramentas Utilizadas

(Extração)
- Web Scraping
- Scrapy
(Transformação)
- Python
- Pandas
(Carregamento e visualização)
- Streamlit

## Como rodar a aplicação

1. A primeira coisa a se fazer é gerar um ambiente virtual. Isso garantirá o bom funcionamento do código e evitará possíveis conflitos.
   Execute o comando python -m venv .venv
   Depois execute source .venv/Scripts/activate (git bash)
   ou simplesmente .venv/Scripts/activate (prompt de comando)

2. Instale as dependências do projeto
   pip install -r requirements.txt

3. Garanta que você está executando o terminal a partir do diretorio _src_
   cd src

4. Execute a extração de dados com o Scrapy
   scrapy crawl mercadolivre -o ../data/data.jsonl

5. Execute a transformação dos dados
   python transformacao/main.py

   Se, por algum motivo, a transformação falhar você pode utilizar o arquivo _.json_ de amostra apenas substituindo a linha
   dataFrame = pd.read_json('../data/data.jsonl', lines=True)
   por
   dataFrame = pd.read_json('../data/data.json')
   no arquivo transformacao/main.py

6. Execute o Streamlit para gerar o dashboard
   streamlit run dashboard/app.py
   você deverá ser redirecionado para uma página web. Caso isso não ocorra confira seu terminal por um link local e um da web
# ETL Pipeline for Price Monitoring

## Contents

### _EN-US_
- [Description](#description)
- [Objective](#objective)
- [Tools used](#tools-used)
- [How to run](#how-to-run)

### _PT-BR_
- [Descrição](#descrição)
- [Objetivo](#objetivo)
- [Ferramentas Utilizadas](#ferramentas-utilizadas)
- [Como rodar a aplicação](#como-rodar-a-aplicação)

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
- Web Scraping
- Scrapy
- Python
- Pandas
- Streamlit

## How to run

   1. ### Configure the virtual environment:
      This will insure the good functioning and will avoid possible conflicts. Execute the following commands:
      
      ```
      python -m venv .venv
      ```
      After that, activate the virtual environment through `Git Bash`
      
      ```bash
      source .venv/Scripts/activate
      ```
      or through `Command Prompt`:
      
      ```prompt de comando
      .venv/Scripts/activate
      ```
      
   2. ### Install dependencies:
      ```
      pip install -r requirements.txt
      ```
   
   3. ### Navigate to the _src_ folder:  
      Make sure you are running your terminal since the `src` folder:
      ```
      cd src
      ```
      
   4. ### Execute data extraction using Scrapy:
      ```
      scrapy crawl mercadolivre -o ../data/data.jsonl
      ```
      
   5. ### Execute data transformation:
      ```
      python transformacao/main.py
      ```
      If, for any reason, the transformation fails you can use the _data.json_ example file. Just replace the following code line in the file `transformacao/main.py`:
      ```python
      dataFrame = pd.read_json('../data/data.jsonl', lines=True)
      ```
      for:
      ```python
      dataFrame = pd.read_json('../data/data.json')
      ```
      
   6. ### Execute Streamlit to generate the dashboard 
      ```
      streamlit run dashboard/app.py
      ```
      You should be redirected to a web page. If it doesn't happen check your terminal for a local and a web link.

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
- Web Scraping
- Scrapy
- Python
- Pandas
- Streamlit

## Como rodar a aplicação

   1. ### Configurar o ambiente virtual:
      Isso garantirá o bom funcionamento do código e evitará possíveis conflitos. Execute os seguintes comandos:
      
      ```
      python -m venv .venv
      ```
      Depois, ative o ambiente virtual através do `Git Bash`
      
      ```bash
      source .venv/Scripts/activate
      ```
      ou pelo `Prompt de Comando`:
      
      ```prompt de comando
      .venv/Scripts/activate
      ```
      
   2. ### Instalar dependências:
      ```
      pip install -r requirements.txt
      ```
   
   3. ### Navegar para o diretório _src_:  
      Garanta que você está executando o terminal a partir do diretório `src`:
      ```
      cd src
      ```
      
   4. ### Executar a extração de dados com o Scrapy:
      ```
      scrapy crawl mercadolivre -o ../data/data.jsonl
      ```
      
   5. ### Executar a transformação dos dados:
      ```
      python transformacao/main.py
      ```
      Se, por algum motivo, a transformação falhar, você pode utilizar o arquivo _.json_ de amostra. Basta substituir a linha a seguir no arquivo `transformacao/main.py`:
      ```python
      dataFrame = pd.read_json('../data/data.jsonl', lines=True)
      ```
      por:
      ```python
      dataFrame = pd.read_json('../data/data.json')
      ```
      
   6. ### Executar o Streamlit para gerar o dashboard:
      ```
      streamlit run dashboard/app.py
      ```
      Você deverá ser redirecionado para uma página web. Caso isso não ocorra, confira seu terminal por um link local e um da web.

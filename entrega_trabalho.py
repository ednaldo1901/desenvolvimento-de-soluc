import pandas as pd

print(pd.__version__)

df = pd.read_csv('baseDados.csv', sep=';')
print(df.head())

df_subset = df[['ID', 'Duration', 'Calories']]
print(df_subset.head()) 

pd.set_option('display.max_rows', 9999)
print(df.to_string())

print("Primeiras 10 linhas do conjunto de dados original:")
print(df.head(10).to_string())

print("\nÚltimas 10 linhas do conjunto de dados original:")
print(df.tail(10).to_string())

print(df.info())

df_tratado = df.copy()
import numpy as np
df_tratado['Date'] = df_tratado['Date'].replace('1900/01/01', np.nan)
print("Primeiras linhas do DataFrame 'df_tratado' após a substituição:")
print(df_tratado.head())

df_tratado['Date'] = pd.to_datetime(df_tratado['Date'], errors='coerce')
print("Informações do DataFrame 'df_tratado' após conversão da coluna 'Date':")
print(df_tratado.info())
print("\nPrimeiras linhas do DataFrame 'df_tratado' após conversão da coluna 'Date':")
print(df_tratado.head())

original_date_string = '20201226'

corrected_datetime = pd.to_datetime(original_date_string, format='%Y%m%d')

df_tratado.loc[26, 'Date'] = corrected_datetime

print("Linhas do DataFrame 'df_tratado' após a correção específica do valor '20201226':")
print(df_tratado.loc[25:27])

df_tratado['Date'] = pd.to_datetime(df_tratado['Date'], errors='coerce')

print("Informações do DataFrame 'df_tratado' após a conversão final da coluna 'Date':")
print(df_tratado.info())

print("\nPrimeiras 5 linhas do DataFrame 'df_tratado' após a conversão final da coluna 'Date':")
print(df_tratado.head())

print("\nÚltimas 5 linhas do DataFrame 'df_tratado' após a conversão final da coluna 'Date':")
print(df_tratado.tail())

df_tratado.dropna(subset=['Date'], inplace=True)

print("Informações do DataFrame 'df_tratado' após a remoção de valores nulos na coluna 'Date':")
print(df_tratado.info())

print("Primeiras 5 linhas do DataFrame 'df_tratado':")
print(df_tratado.head())

print("\nÚltimas 5 linhas do DataFrame 'df_tratado':")
print(df_tratado.tail())

print("\nInformações do DataFrame 'df_tratado' (final):")
print(df_tratado.info())

print("\nNúmero de valores nulos na coluna 'Date':")
print(df_tratado['Date'].isnull().sum())
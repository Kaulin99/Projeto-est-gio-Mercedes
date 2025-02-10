#!pip install pandas pyarrow
import pandas as pd

# Carregue o arquivo Parquet
file_path = "C:/Users/kauea/OneDrive/Área de Trabalho/ERROR 404/Faculdade/Estágio/Case/Case/cod_pais.parquet"
df = pd.read_parquet(file_path)

# Visualize as primeiras linhas
print(df.head())

# Verificar colunas e tipos
print(df.info())

# Verificar estatísticas básicas
print(df.describe())

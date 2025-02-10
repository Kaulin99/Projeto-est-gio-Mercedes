#!pip install pandas pyarrow
import pandas as pd
import matplotlib.pyplot as plt

# Carregue o arquivo Parquet
file_path = "C:/Users/kauea/OneDrive/Área de Trabalho/ERROR 404/Faculdade/Estágio/Case/Case/veiculos.parquet"
df = pd.read_parquet(file_path)

# Visualize as primeiras linhas
#print(df.head())

# Verificar colunas e tipos
#print(df.info())

# Verificar estatísticas básicas
#print(df.describe())

# Filtrar apenas veículos de um certo tipo
#filtered_df = df[df["Denominação"] == "O-500U 1826/59 EURO5"]
#print(filtered_df)

# Criar uma coluna calculada (exemplo)
#df["DTLCO"] = pd.to_datetime(df["DTLCO"]).dt.year
#print(df)

#df["Denominação"].value_counts().plot(kind="line")
#plt.show()

# Exemplo de combinar bases
df2 = pd.read_parquet("C:/Users/kauea/OneDrive/Área de Trabalho/ERROR 404/Faculdade/Estágio/Case/Case/cod_pais.parquet")
merged_df = pd.merge(df, df2, on="CodPais")

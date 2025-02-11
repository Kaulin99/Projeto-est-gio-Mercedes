import pandas as pd
import matplotlib.pyplot as plt
import openpyxl as op

# Carregue o arquivo Parquet
file_path = "C:/Users/kauea/OneDrive/Área de Trabalho/ERROR 404/Faculdade/Projeto-est-gio-Mercedes/Case/Case/veiculos.parquet"
Tabela1 = pd.read_parquet(file_path)

# Carrega o arquivo Parquet com os dados dos países
Tabela2 = pd.read_parquet("C:/Users/kauea/OneDrive/Área de Trabalho/ERROR 404/Faculdade/Projeto-est-gio-Mercedes/Case/Case/cod_pais.parquet")

# Renomear colunas para facilitar integração
Tabela1.rename(columns={'CodPais': 'Codigo_Pais', 'Denominação': 'Tipo_Veiculo', 
                    'varNED': 'Subtipo_Veiculo', 'NP': 'Numero_Registro', 
                    'DTFLI': 'Data_Producao', 'DTLCO_1a': 'Data_Liberacao_Parcial',
                    'DTLCO': 'Data_Liberacao_Completa', 'DTFAT': 'Data_Faturamento'}, inplace=True)
Tabela2.rename(columns={'COD': 'Codigo_Pais'}, inplace=True)

#Converte para DateTime os dados em object que precisam ser manipulados como data
date_columns = ['Data_Producao', 'Data_Liberacao_Parcial', 'Data_Liberacao_Completa', 'Data_Faturamento']
for col in date_columns:
    Tabela1[col] = pd.to_datetime(Tabela1[col], format='%d%m%y', errors='coerce')

#Inner Join dos dois Parquets
TabelasConjuntas = pd.merge(Tabela1, Tabela2, on=['Codigo_Pais'], how='inner')
print(TabelasConjuntas.head())    

# Remover duplicatas com base na chave primária (Numero_Registro)
Tabela1.drop_duplicates(subset='Numero_Registro', inplace=True)

# Preencher valores ausentes ou tratá-los conforme necessário
Tabela1.fillna({'Tipo_Veiculo': 'Desconhecido', 'Subtipo_Veiculo': 'Indefinido'}, inplace=True)

# Salvar como Excel para trabalhar no PowerBI
#Tabela1.to_excel('TabelaVeiculos.xlsx', index=False, engine='openpyxl')
#Tabela2.to_excel('TabelaPaises.xlsx', index=False, engine='openpyxl')
#TabelasConjuntas.to_excel('TabelaConjunta.xlsx', index=False, engine='openpyxl')

print("Arquivo Excel salvo com sucesso!")
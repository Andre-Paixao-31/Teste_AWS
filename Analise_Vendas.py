# (1) - Implemente uma solução para ler o arquivo 'vendas_grandes.csv' de forma eficiente, considerando o grande volume de dados.

import pandas as pd
import matplotlib
for vendas in pd.read_csv("C:/Users/55119/Desktop/Teste_Leega_Amazon/vendas.csv",sep=",",encoding='ISO-8859-1', chunksize = 5000000):
    vendas.head()
    
vendas.columns.values

ColunasSelecionadas = ['Region', 'Country', 'Item Type', 'Sales Channel','Order Date', 'Units Sold']

vendasSelecionadas = vendas.filter(items=ColunasSelecionadas)

vendasSelecionadas.head()

Q2_colunasSelecionadas = ['Sales Channel', 'Units Sold','Item Type']

Q2_vendas_Sales_Channel_Units_Sold = vendas.filter(items=Q2_colunasSelecionadas)

Q2_vendas_Sales_Channel_Units_Sold.head()

pd.options.display.max_rows = 185
#-------------------------------------------------------------------------------------------------------------------------------------------
# (2) - Identifique o produto mais vendido em termos de quantidade e canal. 
# Resposta: 
# Baby Food = 41.6765 Units Sold

Q2 = Q2_vendas_Sales_Channel_Units_Sold.groupby('Item Type').count()

print(Q2)
#-------------------------------------------------------------------------------------------------------------------------------------------
# (3) - Determine qual pais e região teve o maior volume de vendas (em valor). 
# Respostas: 
#          Região com maior volume de vendas = Sub-Saharan Africa com 6.486.855.992 Units Sold  
#          País com maior volume de vendas = Liberia com 136.188.169 Units Sold  

Q3_colunasSelecionadas = ['Region', 'Country','Units Sold']

Q3_vendas_Region_Country_Units_Sold = vendas.filter(items=Q3_colunasSelecionadas)

Q3_1 = Q3_vendas_Region_Country_Units_Sold.groupby(['Region']).sum('Units Sold').sort_values(by='Units Sold', ascending=False)

print(Q3_1)

Q3_2 = Q3_vendas_Region_Country_Units_Sold.groupby(['Region','Country']).sum('Units Sold').sort_values(by='Units Sold', ascending=False)

print(Q3_2)
#-------------------------------------------------------------------------------------------------------------------------------------------
# (4) - Calcule a média de vendas mensais por produto, considerando o período dos dados disponíveis. Units Sold, Item Type, Order Date
# Respostas: 
#          - Ver lista abaixo, agrupada por (Item Type) e (Month) com o média de (Units Sold)

Q4_colunasSelecionadas = ['Units Sold', 'Item Type','Order Date']

Q4_vendas = vendas.filter(items=Q4_colunasSelecionadas)

date_col = pd.DatetimeIndex(Q4_vendas['Order Date'])
#Q4_vendas['Year'] = date_col.year
Q4_vendas['Month'] = date_col.month
#Q4_vendas['Day'] = date_col.day

Q4_vendas.groupby(['Item Type','Month']).mean('Units Sold')

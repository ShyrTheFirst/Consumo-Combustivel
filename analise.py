import pandas as pd
import matplotlib.pyplot as plt

####################################################################
#           descobrir nome das páginas da planilha:                #
#combustivel = pd.ExcelFile("Controle_Combustivel.xlsx")           #
#                                                                  #
#nomes_das_paginas = combustivel.sheet_names                       #
#                                                                  #
#print(nomes_das_paginas)                                          #
####################################################################

#Carregar planilha dos dados
combustivel_planilha = pd.read_excel('Controle_Combustivel.xlsx', sheet_name= 'Analise_python')

#Separar colunas que serão usadas
valor_gasto = combustivel_planilha['Valor gasto']
litros = combustivel_planilha['Litros']
km_rodado = combustivel_planilha['Km rodada']
tipo = combustivel_planilha['Tipo']


##############################
#     Analisar o seguinte:   #
# Km/L                       #
# Valor/Km                   #
# Valor/L                    #
# Media de Km rodado         #
# L/Km                       #
##############################

#Valor de 50 reais
valor_50 = combustivel_planilha[valor_gasto == 50]
#Valor de 75 reais
valor_75 = combustivel_planilha[valor_gasto == 75]
#Valor de 100 reais
valor_100 = combustivel_planilha[valor_gasto == 100]

#KM rodado para cada valor
km_rodado50 = valor_50['Km rodada']
km_rodado75 = valor_75['Km rodada']
km_rodado100 = valor_100['Km rodada']

#Litros para cada valor
litros50 = valor_50['Litros']
litros75 = valor_75['Litros']
litros100 = valor_100['Litros']

valor_gasto.plot() #### Ainda não funciona no python 3.12 ####

#Plotar:
# x = km_rodado
# y = litros --------- line

# x = valor
# y = km_rodado --------- scatter?

# x = valor
# y = litros --------- line

# somente Km rodada para criar media --------- box type


#### EXEMPLOS E POSSIBILIDADES ####
#air_quality.plot.scatter(x="station_london", y="station_paris", alpha=0.5)
# no exemplo acima,
#dentro da planilha de qualidade do ar,
#pega as colunas station_london e station_paris
#para plota-las no x e y num gráfico tipo scatter.

#['area',
# 'bar',
# 'barh',
# 'box',
# 'density',
# 'hexbin',
# 'hist',
# 'kde',
# 'line',
# 'pie',
# 'scatter']
####



plt.show()








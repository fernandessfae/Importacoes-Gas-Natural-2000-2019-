import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose

#Anexação do ano no índex da variável para a visualização da série temporal
dateparse = lambda dates: pd.datetime.strptime(dates, '%Y')
data = pd.read_csv('importacao-gas-natural-2000-2019-m3.csv', delimiter = ';', decimal = ',',
                   parse_dates = ['ANO'], index_col ='ANO', date_parser = dateparse)

#Transformação da produção de mil m³ para m³ somente
def mul_colunas(lista_features):
    for i in lista_features:
        data[i] = data[i].truediv(1000)
mul_colunas(['JAN','FEV', 'MAR', 'ABR', 'MAI', 'JUN', 'JUL', 'AGO', 'SET', 'OUT', 'NOV', 'DEZ', 'TOTAL'])

#Separação da importação de gás natural de cada mês
data_jan = data.iloc[:, 3]
data_fev = data.iloc[:, 4]
data_mar = data.iloc[:, 5]
data_abr = data.iloc[:, 6]
data_mai = data.iloc[:, 7]
data_jun = data.iloc[:, 8]
data_jul = data.iloc[:, 9]
data_ago = data.iloc[:, 10]
data_set = data.iloc[:, 11]
data_out = data.iloc[:, 12]
data_nov = data.iloc[:, 13]
data_dez = data.iloc[:, 14]

#Visualizaçãodo gráfico e da decomposição da série temporal de cada mês
def decomposicao(series):
    plt.figure(figsize = (10, 5))
    plt.xlabel('Anos')
    plt.ylabel('Quantidade (m³)')
    if series is data_jan:
        plt.title('Quantidade de gás natural importado em janeiro', fontsize = 16, fontweight = 'bold')
    elif series is data_fev:
        plt.title('Quantidade de gás natural importado em fevereiro', fontsize = 16, fontweight = 'bold')
    elif series is data_mar:
        plt.title('Quantidade de gás natural importado em março', fontsize = 16, fontweight = 'bold')
    elif series is data_abr:
        plt.title('Quantidade de gás natural importado em abril', fontsize = 16, fontweight = 'bold')
    elif series is data_mai:
        plt.title('Quantidade de gás natural importado em maio', fontsize = 16, fontweight = 'bold')
    elif series is data_jun:
        plt.title('Quantidade de gás natural importado em junho', fontsize = 16, fontweight = 'bold')
    elif series is data_jul:
        plt.title('Quantidade de gás natural importado em julho', fontsize = 16, fontweight = 'bold')
    elif series is data_ago:
        plt.title('Quantidade de gás natural importado em agosto', fontsize = 16, fontweight = 'bold')
    elif series is data_set:
        plt.title('Quantidade de gás natural importado em setembro', fontsize = 16, fontweight = 'bold')
    elif series is data_out:
        plt.title('Quantidade de gás natural importado em outubro', fontsize = 16, fontweight = 'bold')
    elif series is data_nov:
        plt.title('Quantidade de gás natural importado em novembro', fontsize = 16, fontweight = 'bold')
    elif series is data_dez:
        plt.title('Quantidade de gás natural importado em dezembro', fontsize = 16, fontweight = 'bold')
    plt.plot(series)
    
    decomposicao = seasonal_decompose(series)
    tendencia = decomposicao.trend
    sazonal = decomposicao.seasonal
    residuo = decomposicao.resid
    
    plt.figure(figsize = (10, 5))
    plt.subplot(4, 1, 1)
    if series is data_jan:
        plt.plot(series, label = 'Janeiro')
    elif series is data_fev:
        plt.plot(series, label = 'Fevereiro')
    elif series is data_mar:
        plt.plot(series, label = 'Março')
    elif series is data_abr:
        plt.plot(series, label = 'Abril')
    elif series is data_mai:
        plt.plot(series, label = 'Maio')
    elif series is data_jun:
        plt.plot(series, label = 'Junho')
    elif series is data_jul:
        plt.plot(series, label = 'Julho')
    elif series is data_ago:
        plt.plot(series, label = 'Agosto')
    elif series is data_set:
        plt.plot(series, label = 'Setembro')
    elif series is data_out:
        plt.plot(series, label = 'Outubro')
    elif series is data_nov:
        plt.plot(series, label = 'Novembro')
    elif series is data_dez:
        plt.plot(series, label = 'Dezembro')
    plt.legend(loc = 'best')
    
    plt.subplot(4, 1, 2)
    plt.plot(tendencia, label = 'Tendência')
    plt.legend(loc = 'best')
    
    plt.subplot(4, 1, 3)
    plt.plot(sazonal, label = 'Sazonalidade')
    plt.legend(loc = 'best')
    
    plt.subplot(4, 1, 4)
    plt.plot(residuo, label = 'Residuo')
    plt.legend(loc = 'best')
    plt.tight_layout()

decomposicao(data_jan)
decomposicao(data_fev)
decomposicao(data_mar)
decomposicao(data_abr)
decomposicao(data_mai)
decomposicao(data_jun)
decomposicao(data_jul)
decomposicao(data_ago)
decomposicao(data_set)
decomposicao(data_out)
decomposicao(data_nov)
decomposicao(data_dez)
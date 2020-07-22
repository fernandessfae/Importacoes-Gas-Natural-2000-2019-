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

#Separação dos quadrimestres
data['QUADRIMESTRE1'] = data[['JAN', 'FEV', 'MAR', 'ABR']].sum(axis = 1)
data['QUADRIMESTRE2'] = data[['MAI', 'JUN', 'JUL', 'AGO']].sum(axis = 1)
data['QUADRIMESTRE3'] = data[['SET', 'OUT', 'NOV', 'DEZ']].sum(axis = 1)

q1 = data.iloc[:, 16]
q2 = data.iloc[:, 17]
q3 = data.iloc[:, 18]

#Visualização do gráfico e da decomposição da série temporal de cada quadrimestre
def decomposicao(series):
    plt.figure(figsize = (10, 5))
    plt.xlabel('Anos')
    plt.ylabel('Quantidade (m³)')
    if series is q1:
        plt.title('Quantidade de gás natural importado no 1° quadrimestre', fontsize = 16, fontweight = 'bold')
    elif series is q2:
        plt.title('Quantidade de gás natural importado no 2° quadrimestre', fontsize = 16, fontweight = 'bold')
    elif series is q3:
        plt.title('Quantidade de gás natural importado no 3° quadrimestre', fontsize = 16, fontweight = 'bold')
    plt.plot(series)
    
    decomposicao = seasonal_decompose(series)
    tendencia = decomposicao.trend
    sazonal = decomposicao.seasonal
    residuo = decomposicao.resid
    
    plt.figure(figsize = (10, 5))
    plt.subplot(4, 1, 1)
    if series is q1:
        plt.plot(series, label = '1° quadrimestre')
    elif series is q2:
        plt.plot(series, label = '2° quadrimestre')
    elif series is q3:
        plt.plot(series, label = '3° quadrimestre')
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
    
decomposicao(q1)
decomposicao(q2)
decomposicao(q3)
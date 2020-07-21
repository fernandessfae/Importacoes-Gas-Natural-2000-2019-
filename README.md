# Importações gás natural em mil m³ (2000-2019)
Aqui irá mostrar a quantidade de gás natural importado pelo Brasil nos anos de 2000 até 2019. Esse dados são encontrados [aqui](http://dados.gov.br/dataset/importacoes-gas-natural).
OBS: Como no momento que estava fazendo as análises desses dados, o valor referente a dezembro de 2019 não estava preenchido, então resolvi tirar a média de todos os meses de dezembro de 2000 a 2018 para colocar em dezembro de 2019.

## Análise Exploratória de Dados
A ideia é ver as informações importante dessa base de dados, e verificar o que pode ser relevante através deles.

### Histograma

**Mensal**
![importação mensal](https://user-images.githubusercontent.com/48027825/88097667-e5c5ad80-cb6e-11ea-9049-7be7c9a2572e.png)

**Bimestral**
![importação bimestral](https://user-images.githubusercontent.com/48027825/88097658-e52d1700-cb6e-11ea-8a39-1712c018c6ba.png)

**Trimestral**
![importação trimestral](https://user-images.githubusercontent.com/48027825/88097671-e6f6da80-cb6e-11ea-8b8e-4e8e673faea5.png)

**Quadrimestral**
![importação quadrimestral](https://user-images.githubusercontent.com/48027825/88097668-e65e4400-cb6e-11ea-8c00-849d5ebc5337.png)

**Semestral**
![importação semestral](https://user-images.githubusercontent.com/48027825/88097669-e65e4400-cb6e-11ea-9eae-5112ef3fcdad.png)

**Anual**
![importação anual](https://user-images.githubusercontent.com/48027825/88097673-e6f6da80-cb6e-11ea-84ad-8438ebe144ff.png)

## Decomposição da série temporal

- Anual

![Figure_1](https://user-images.githubusercontent.com/48027825/73229964-71c7c100-415a-11ea-89eb-4a8204872b9b.png)

## Gráfico da série temporal (anual), com diferenciação, para o teste de estacionariedade

![Figure_1](https://user-images.githubusercontent.com/48027825/73398104-97240e80-42c3-11ea-9db4-72cb352f763e.png)

## Teste de estacionariedade (anual)

**Dickey Fuller e KPSS**

Resultado do Teste Dickey-Fuller para o ano : <br/>
Teste                    -6.625049e+00<br/>
Valor p                   5.905020e-09<br/>
 de lags                  7.000000e+00<br/>
 de observações           1.000000e+01<br/>
Valores críticos (1%)    -4.331573e+00<br/>
Valores críticos (5%)    -3.232950e+00<br/>
Valores críticos (10%)   -2.748700e+00

H0 = A série não é estacionária. <br/>
H1 = A série é estacionária.

Resultado com o teste KPSS para o ano:<br/>
Status KPSS                                                         0.317492<br/>
Valor p                                                                  0.1<br/>
 de lags                                                                  9<br/>
 de observações           
Valores críticos (10%)                                                 0.347<br/>
Valores críticos (5%)                                                  0.463<br/>
Valores críticos (2.5%)                                                0.574<br/>
Valores críticos (1%)                                                  0.739

H0 = A série é estacionária. <br/>
H1 = A série apresenta raiz unitária.

## Teste de tendência (anual)

**Mann-Kendall**

Resultado do Teste Mann-Kendall<br/>
Movimento Tendência     increasing<br/>
Há Tendência?                 True<br/>
Valor p                0.000112984<br/>
Teste normalizado          3.86087<br/>
Coeficiente Kendall       0.631579<br/>
Mand-Kendall Score             120<br/>
Variância S                    950<br/>
Sen Slope                   670084<br/>

H0 = As observações da série são independentes e identicamente distribuídas. (Não há tendência)<br/>
H1 = As observações da série possuem tendência monotônica no tempo. (Há tendência)

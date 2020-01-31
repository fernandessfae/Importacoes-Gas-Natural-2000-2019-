# Importações gás natural em mil m³ (2000-2019)
Mostra o quanto de gás natural foi importado pelo Brasil nos anos de 2000 até 2019, e as possiveis tendências para os próximos anos.<br/>
Link do dataset: http://dados.gov.br/dataset/importacoes-gas-natural<br/>
OBS: Como no momento que estava fazendo as análises desses dados, o valor referente a dezembro de 2019 não estava preenchido, então resolvi tirar a média de todos os meses de dezembro de 2000 a 2018 para colocar em dezembro de 2019.

## A ideia é verificar se existe alguma informação importante para essa base de dados.

### Histograma

- Mensal

![Figure_1](https://user-images.githubusercontent.com/48027825/73208118-a882e480-4124-11ea-8b99-23a0a7c0bf4b.png)

- Bimestral

![Figure_2](https://user-images.githubusercontent.com/48027825/73208119-a91b7b00-4124-11ea-9331-41dfbd94047b.png)

- Trimestral

![Figure_3](https://user-images.githubusercontent.com/48027825/73208120-a91b7b00-4124-11ea-8013-d5ce6ec77e8b.png)

- Quadrimestral

![Figure_4](https://user-images.githubusercontent.com/48027825/73208121-a91b7b00-4124-11ea-84dc-9d907ce90f58.png)

- Semestral

![Figure_5](https://user-images.githubusercontent.com/48027825/73208122-a91b7b00-4124-11ea-9e2e-d8d8d8d44a21.png)

- Anual

![Figure_6](https://user-images.githubusercontent.com/48027825/73208123-a9b41180-4124-11ea-9b58-a290ce4befea.png)

## Gráfico dos dados anuais

![Figure_1](https://user-images.githubusercontent.com/48027825/73303356-1b5b9080-41f5-11ea-9227-063fa79522e6.png)

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

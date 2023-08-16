# Para o ano de 1991, compare a População Urbana entre os estados usando um
# gráfico de barras

import matplotlib.pyplot as plt
import pandas as pd
dado= pd.read_csv(r"D:\Downloads\Dataset_Processo_Seletivo_UFRJ_Analytica_2022.1.csv")
pop= dado['populacao_rural']
estados = dado['sigla_uf']
plt.bar(estados, pop, color="tomato")
plt.title('População Urbana entre estados')
plt.xlabel('Estados')
plt.ylabel('População')
plt.show()



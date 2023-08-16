# Utilizando a mesma base de dados, obtenha a diferença de expectativa de vida
# de cada estado entre os anos de 1991 e 2010. Faça um gráfico de barras com esses
# valores. Retorne todos os estados que tiveram um aumento de pelo menos 10 anos
# na expectativa de vida entre 1991 e 2010.

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
dado= pd.read_csv(r"D:\Downloads\Dataset_Processo_Seletivo_UFRJ_Analytica_2022.1.csv")

dados_1991 = dado[dado['ano'] == 1991]
dados_2010 = dado[dado['ano'] == 2010]

dadomerge= pd.merge (dados_1991, dados_2010, how= 'outer', on='sigla_uf')
dadomerge['diferença']=  dadomerge['expectativa_vida_y'] - dadomerge['expectativa_vida_x']
estadosacima10anos = dadomerge[dadomerge['diferença'] > 10] 


plt.bar(estadosacima10anos['sigla_uf'], estadosacima10anos['diferença'], color='turquoise')
plt.xlabel('Estado')
plt.ylabel('Diferença de Expectativa de Vida entre os anos de 2010 e 1991)')
plt.title('Estados com Aumento de 10 Anos na Expectativa de Vida entre 1991 e 2010')
plt.tight_layout()
plt.show()
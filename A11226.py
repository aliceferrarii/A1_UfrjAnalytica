#Analise os dados de IDH. Use as funções de .min(), .max(), .idxmin() e .idxmax()
#para saber qual o estado de maior e menor IDH no DataFrame do ano de 1991.

#Está imprimindo o IDH médio da A11223
import pandas as pd
import numpy as np
from A11223 import idh, dados_1991

maximo = dados_1991['idhm'].max()
indexmax = dados_1991['idhm'].idxmax()
estado_max_idh = dados_1991.loc[indexmax, 'sigla_uf']

minimo = dados_1991['idhm'].min()
indexmin = dados_1991['idhm'].idxmin()
estado_min_idh = dados_1991.loc[indexmin, 'sigla_uf']

print(f"O estado com maior IDH é: {estado_max_idh} com IDH: {maximo}")
print(f"O estado com menor IDH é: {estado_min_idh} com IDH: {minimo}")


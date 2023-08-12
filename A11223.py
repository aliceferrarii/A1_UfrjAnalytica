#Calcule o IDH médio do brasil no ano de 1991:
import pandas as pd
import numpy as np
dados = pd.read_csv(r"D:\Downloads\Dataset_Processo_Seletivo_UFRJ_Analytica_2022.1.csv")
dados_1991 = dados[dados['ano'] == 1991]
idh = dados_1991['idhm']
print (f"O IDH médio do ano de 1991 é: {np.mean(idh)}")

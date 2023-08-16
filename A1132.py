# Faça um gráfico de histograma do IDH dos estados do Brasil para cada
# ano existente nos dados e compare a evolução da desigualdade.

import matplotlib.pyplot as plt
import pandas as pd
dado= pd.read_csv(r"D:\Downloads\Dataset_Processo_Seletivo_UFRJ_Analytica_2022.1.csv")

dados_1991=dado[dado['ano'] == 1991]
idh_1991=dados_1991['idhm']

dados_2000=dado[dado['ano'] == 2000]
idh_2000=dados_2000['idhm']

dados_2010=dado[dado['ano'] == 2010]
idh_2010=dados_2010['idhm']

plt.subplot(3,1,1)
plt.hist(idh_1991, bins=27, color='purple', alpha=0.7)
plt.title('IDH em 1991')

plt.subplot(3, 1, 2)
plt.hist(idh_2000, bins=27, color='cyan', alpha=0.7)
plt.title('IDH em 2000')

plt.subplot(3, 1, 3)
plt.hist(idh_2010, bins=27, color='pink', alpha=0.7)
plt.title('IDH em 2010')

plt.tight_layout()
plt.show()



# Faça um gráfico desse tipo (Scatter Plot) e analise se
# existe alguma tendência clara.



import matplotlib.pyplot as plt
import pandas as pd
dado= pd.read_csv(r"D:\Downloads\Dataset_Processo_Seletivo_UFRJ_Analytica_2022.1.csv")

vida= dado['expectativa_vida']
idh= dado['idhm']

plt.xlabel('Expectativa de Vida')
plt.ylabel('IDH')

plt.scatter(vida, idh, color='darkkhaki')
plt.show()

#Existe sim uma tendência de aumento de expectativa de vida (EV) conforme há aumento de IDH,
#visto que há formação de um linha em que a cada aumento de IDH, há também aumento de EV. 
#A partir da lista dos IDHs da questão anterior retorne o estados que estão acima
#da média, também no ano de 1991.


#Está imprimindo o IDH médio da A11223
import pandas as pd
import numpy as np
from A11223 import idh, dados_1991
idh_maior_que_a_media = dados_1991[ dados_1991["idhm"] > np.mean(idh)]["sigla_uf"]
estados = ", ".join(idh_maior_que_a_media.tolist())
print(f"Os estados que possuem IDH acima da média são: {estados}")

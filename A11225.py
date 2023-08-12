#Ordene os dados do DataFrame de 1991 de acordo com o IDH, usando a função
#sort values() e mostre a tabela dos 5 primeiros com o .head(5).

#Está imprimindo o IDH médio da A11223
import pandas as pd
from A11223 import idh, dados_1991
ordenado=idh.sort_values()
print(ordenado.head(5))